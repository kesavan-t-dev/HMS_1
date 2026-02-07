from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count
from django.db import IntegrityError
from .models import doctors, slots, patients, mapping


def root_redirect(request):
    return redirect('home')


def book_appointment(request):
    doctor_list = doctors.objects.values('id', 'name')
    error = ""

    if request.method == 'POST':
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age') or None
        doctor_id = request.POST.get('doctor')
        date_str = request.POST.get('date')
        slot_id = request.POST.get('slot')
        reason = request.POST.get('reason', "")

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except:
            date_obj = None

        if age is not None:
            try:
                age = int(age)
            except:
                age = None

        if not (phone and name and gender and doctor_id and date_obj and slot_id):
            error = "Please fill all required fields."
            return render(request, 'form.html', {'doctor': doctor_list, 'error': error})

        doctor_obj = doctors.objects.filter(id=doctor_id).first()
        slot_obj = slots.objects.filter(id=slot_id).first()

        if not doctor_obj or not slot_obj:
            error = "Invalid doctor or slot selected."
            return render(request, 'form.html', {'doctor': doctor_list, 'error': error})

        patient, created = patients.objects.get_or_create(
            phone_no=phone,
            defaults={'name': name, 'gender': gender, 'age': age}
        )

        if mapping.objects.filter(is_booked=True, doctor=doctor_obj, date=date_obj, slot=slot_obj).exists():
            error = "This slot is already booked for the selected doctor."
            return render(request, 'form.html', {'doctor': doctor_list, 'error': error})

        booking = mapping.objects.create(
            patient=patient,
            doctor=doctor_obj,
            slot=slot_obj,
            date=date_obj,
            reason=reason,
            is_booked=True
        )

        request.session['last_booking_id'] = str(booking.id)
        return redirect('success')

    return render(request, 'form.html', {'doctor': doctor_list, 'error': error})



def slot_availability(request):
    date_str = request.GET.get('date')
    doctor_id = request.GET.get('doctor')

    if not date_str or not doctor_id:
        return JsonResponse({'slots': [], 'unavailable': [], 'slot_full': []})

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({'slots': [], 'unavailable': [], 'slot_full': []})

    all_slots = list(slots.objects.values('id', 'start_time', 'end_time'))

    unavailable_qs = (
        mapping.objects
        .filter(is_booked=True, date=date_obj, doctor_id=doctor_id)
        .values_list('slot_id', flat=True)
    )
    unavailable = [str(x) for x in unavailable_qs]

    total_doctors = doctors.objects.count()

    slot_full_qs = (
        mapping.objects
        .filter(is_booked=True, date=date_obj)
        .values('slot_id')
        .annotate(booked_count=Count('doctor_id', distinct=True))
        .filter(booked_count__gte=total_doctors)
        .values_list('slot_id', flat=True)
    )
    slot_full = [str(x) for x in slot_full_qs]

    return JsonResponse({
        'slots': all_slots,
        'unavailable': unavailable,
        'slot_full': slot_full
    })

def booking_success(request):
    booking_id = request.session.get('last_booking_id')

    if not booking_id:
        return render(request, 'confirmation.html', {'booking': None})

    booking = mapping.objects.filter(id=booking_id).select_related('patient', 'doctor', 'slot').first()

    return render(request, 'confirmation.html', {'booking': booking})