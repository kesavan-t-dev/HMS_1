document.addEventListener("DOMContentLoaded", function () {
    const date_input = document.getElementById('date');
    const doctors = document.getElementById('doctor');
    const slots = document.getElementById('slot');

    function update_availability() {
        const selected_date = date_input.value;
        const selected_doctor = doctors.value;

        for (let option of slots.options) {
            option.disabled = false;
            option.textContent = option.textContent.replace(" (Full)", "").replace(" (Booked)", "");
        }

        if (!selected_date) return;

        if (slot_data[selected_date]) {
            slot_data[selected_date].forEach(slotId => {
                for (let option of slots.options) {
                    if (option.value === slotId) {
                        option.disabled = true;
                        option.textContent += " (Full)";
                    }
                }
            });
        }

        if (selected_doctor && doctorBookedData[selected_date] && doctorBookedData[selected_date][selected_doctor]) {
            doctorBookedData[selected_date][selected_doctor].forEach(slotId => {
                for (let option of slots.options) {
                    if (option.value === slotId) {
                        option.disabled = true;
                        option.textContent += " (Booked)";
                    }
                }
            });
        }
    }

    date_input.addEventListener('change', update_availability);
    doctors.addEventListener('change', update_availability);
});
