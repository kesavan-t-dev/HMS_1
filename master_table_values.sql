
-- Master table
INSERT INTO <app_name>_doctors (id, name, specialization, gender, phone_no)
VALUES
(gen_random_uuid(), 'Dr. Arjun', 'Cardiology', 'M', '9876543210'),
(gen_random_uuid(), 'Dr. Amal Davis', 'Orthopedics', 'F', '9876543211'),
(gen_random_uuid(), 'Dr. Raj Kumar', 'Neurology', 'M', '9876543212'),
(gen_random_uuid(), 'Dr. Sarah Corner', 'Dermatology', 'F', '9876543213');

INSERT INTO <app_name>_slots (id, start_time, end_time)
VALUES
(gen_random_uuid(), '09:00:00', '09:30:00'),
(gen_random_uuid(), '09:30:00', '10:00:00'),
(gen_random_uuid(), '10:00:00', '10:30:00'),
(gen_random_uuid(), '10:30:00', '11:00:00'),
(gen_random_uuid(), '11:00:00', '11:30:00'),
(gen_random_uuid(), '11:30:00', '12:00:00')