from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor, Patient, Appointment, Prescription, MedicalRecord, Payment, VideoCallLog,Feedback

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'specialization']
    search_fields = ['doctor__username', 'email']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'medical_history']
    search_fields = ['patient__username', 'email']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'date', 'time_slot', 'status']
    list_filter = ['status', 'date']
    search_fields = ['patient__username', 'doctor__username', 'status']

# Prescription Admin
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'appointment', 'doctor', 'patient']
    search_fields = ['appointment__id', 'doctor__username', 'patient__username']

# Medical Record Admin
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'diagnosis', 'created_at']
    search_fields = ['patient__username', 'doctor__username', 'diagnosis']

# Payment Admin
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'appointment', 'amount', 'transaction_id', 'status', 'payment_date']
    list_filter = ['status', 'payment_date']
    search_fields = ['user__username', 'transaction_id']

# Video Call Log Admin
@admin.register(VideoCallLog)
class VideoCallLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'caller', 'receiver', 'start_time', 'end_time', 'duration']
    search_fields = ['caller__username', 'receiver__username']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['id','doctor','patient','rating','date_created']
    search_fields=['doctor','rating']

