from rest_framework import viewsets
from .models import Doctor, Patient, Appointment, Prescription, MedicalRecord, Payment, VideoCallLog,Feedback
from .serializers import (
    DoctorSerializer,DoctorloginSerializer, PatientSerializer, AppointmentSerializer, DoctorregisterSerializer,
    PrescriptionSerializer, MedicalRecordSerializer, PaymentSerializer, VideoCallLogSerializer,FeedbackSerializer,
    PatientregisterSerializer, PatientloginSerializer
)
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from api.custom_permission import *
from django.contrib.auth import get_user_model

def get_tokens_for_doctor(user):
    refresh = RefreshToken.for_user(user)
    refresh['is_doctor'] = user.is_doctor
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def get_tokens_for_patient(user):
    refresh = RefreshToken.for_user(user)
    refresh['is_patient'] = user.is_patient
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Doctor ViewSet
class DoctorRegisterViewSet(views.APIView):
    def post(self, request, format=None):
        serializer = DoctorregisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'Data':'Doctor Registred'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DoctorLoginViewSet(views.APIView):
    def post(self, request, format=None):
        serializer = DoctorloginSerializer(data=request.data)
        print("serializer", serializer)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = Doctor.objects.filter(username=username).first()
            # print("Database User Found:", user)
            if user and user.check_password(password):
                print("Password Matched!")
            # user = authenticate(username=username, password=password)
            # if user is not None:
                token = get_tokens_for_doctor(user)
                return Response({'token':token,'data':'Doctor Login success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['username or password not a valid']}},
                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PatientRegisterViewSet(views.APIView):
    def post(self, request, format=None):
        serializer = PatientregisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'Data':'Patient Registred'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PatientLoginViewSet(views.APIView):
    def post(self, request, format=None):
        serializer = PatientloginSerializer(data=request.data)
        print("serializer", serializer)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            # user = authenticate(username=username, password=password)
            user = Patient.objects.filter(username=username).first()
            if user and user.check_password(password):
                print("Password Matched!")
                token = get_tokens_for_patient(user)
                return Response({'token':token,'data':'Patient Login success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['username or password not a valid']}},
                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# Patient ViewSet
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

# Appointment ViewSet
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

# Prescription ViewSet
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

# Medical Record ViewSet
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

# Payment ViewSet
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

# Video Call Log ViewSet
class VideoCallLogViewSet(viewsets.ModelViewSet):
    queryset = VideoCallLog.objects.all()
    serializer_class = VideoCallLogSerializer
    permission_classes = [IsAuthenticated]

class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]