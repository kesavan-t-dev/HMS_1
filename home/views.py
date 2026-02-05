from django.shortcuts import render, redirect, get_object_or_404
from .models import doctors, slots, patients, mapping
from django.db.models import Count
from datetime import date

def root_redirect(request):
    return redirect('home')  


def book_appointment(request):
    doctor_list = doctors.objects.all()
    slot_list = slots.objects.all()
    booked_slots = []
    selected_date = None

    if request.method == 'POST':
        phone = request.POST.get('phone_no')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age') or None
        doctor_id = request.POST.get('doctor')
        selected_date = request.POST.get('date')
        slot_id = request.POST.get('slot')
        reason = request.POST.get('reason')

        if selected_date:
            booked_slots = []
            total_doctors = doctor_list.count()
            for s in slot_list:
                total_doctors = doctor_list.count()
                booked_count = mapping.objects.filter(slot=s, date=selected_date).values('doctor').distinct().count()
                if booked_count >= total_doctors:
                    booked_slots.append(s.id)


        if phone and name and gender and doctor_id and selected_date and slot_id:
            doctor_obj = get_object_or_404(doctors, id=doctor_id)
            slot_obj = get_object_or_404(slots, id=slot_id)

            patient, created = patients.objects.get_or_create(
                phone_no=phone,
                defaults={
                    'name': name,
                    'gender': gender,
                    'age': age,
                    
                }
            )

            booking = mapping.objects.create(
                patient=patient,
                doctor=doctor_obj,
                slot=slot_obj,
                date=selected_date,
                reason=reason
            )

            return redirect('success', booking_id=booking.id)

    return render(request, 'form.html', {
        'doctor': doctor_list,
        'slots': slot_list,
        'booked_slots': booked_slots,
        'selected_date': selected_date
    })


def booking_success(request, booking_id):
    booking = get_object_or_404(mapping, id=booking_id)
    return render(request, 'confirmation.html', {'booking': booking})
