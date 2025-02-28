from rest_framework import serializers
from .models import Doctor, Patient, Appointment, Prescription, MedicalRecord, Payment, VideoCallLog, Feedback
from django.contrib.auth import get_user_model

User=get_user_model()
# Doctor Serializer
class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'email', 'specialization', 'experience', 'qualification', 'clinic_address', 'available_days', 'available_time_slots']

# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = Patient
        fields = ['id', 'username', 'email', 'date_of_birth', 'gender', 'medical_history']

# Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time_slot', 'status']

# Prescription Serializer
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'appointment', 'doctor', 'patient', 'medicines', 'instructions']

# Medical Record Serializer
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'report_file', 'created_at']

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'patient', 'appointment', 'amount', 'transaction_id', 'status', 'payment_date']

# Video Call Log Serializer
class VideoCallLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCallLog
        fields = ['id', 'caller', 'receiver', 'start_time', 'end_time', 'duration']

# Feedback Serializer
class FeedbackSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'doctor', 'patient', 'rating', 'comments', 'date_created']

class DoctorregisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Doctor
        fields = ['username', 'email','specialization','experience','qualification','clinic_address','available_days','available_time_slots','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        p1 = data.get('password')
        p2 = data.get('password2')
        if p1 != p2:
            raise serializers.ValidationError('Password & confirm password do not match')
        return data

    def create(self, validated_data):
        # Remove the password2 field from validated_data as it's not needed for user creation
        validated_data.pop('password2', None)
        # Create the user with the remaining validated_data
        return Doctor.objects.create_user(**validated_data)
        # password = validated_data.pop('password')  # Extract password
        # user = Doctor(**validated_data)  # Create user instance
        # user.set_password(password)  # Hash password before saving
        # user.save()
        # return user
    
class DoctorloginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','password']

class PatientregisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Patient
        fields = ['username', 'email','date_of_birth','gender','medical_history','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        p1 = data.get('password')
        p2 = data.get('password2')
        if p1 != p2:
            raise serializers.ValidationError('Password & confirm password do not match')
        return data

    def create(self, validated_data):
        # Remove the password2 field from validated_data as it's not needed for user creation
        validated_data.pop('password2', None)
        return Doctor.objects.create_user(**validated_data)

    
class PatientloginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','password']