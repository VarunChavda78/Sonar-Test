from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class Doctor(AbstractUser):
    specialization = models.CharField(max_length=255)
    experience = models.IntegerField()
    qualification = models.CharField(max_length=255)
    clinic_address = models.TextField()
    available_days = models.JSONField()  # Example: ["Monday", "Wednesday", "Friday"]
    available_time_slots = models.JSONField()  # Example: ["10:00 AM - 12:00 PM", "3:00 PM - 5:00 PM"]
    groups = models.ManyToManyField(Group, related_name="doctor_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="doctor_user_permissions", blank=True)
    is_doctor=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}"

class Patient(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    medical_history = models.TextField()
    groups = models.ManyToManyField(Group, related_name="patient_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="patient_user_permissions", blank=True)
    is_patient=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}"


# Appointment
class Appointment(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('canceled', 'Canceled')]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Appointment - {self.patient.username} with Dr. {self.doctor.get_full_name()} on {self.date} at {self.time_slot}"

# Prescription
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="prescription")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_prescriptions")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_prescriptions")
    medicines = models.JSONField()  # [{"name": "Paracetamol", "dosage": "500mg"}]
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.patient.get_full_name()} by Dr. {self.doctor.get_full_name()}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField()
    report_file = models.FileField(upload_to="medical_reports/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.get_full_name()} - {self.diagnosis[:20]}"

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="payments")
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=15, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.patient.username} - {self.status}"

class VideoCallLog(models.Model):
    caller = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="caller_calls")
    receiver = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="receiver_calls")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)  # Auto-calculated

    def __str__(self):
        return f"Call from {self.caller.username} to {self.receiver.username}"

class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_feedbacks')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_feedbacks")
    rating = models.PositiveIntegerField()  # Rating out of 5, for example
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.doctor.username} by {self.patient.username}"