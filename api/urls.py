from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorRegisterViewSet,DoctorLoginViewSet, PatientViewSet, AppointmentViewSet, 
    PrescriptionViewSet, MedicalRecordViewSet, PaymentViewSet, VideoCallLogViewSet,
    FeedbackViewset,PatientRegisterViewSet,PatientLoginViewSet
)
# urlpatterns = [
#     path('doctors/',DoctorViewSet.as_view(),name='doctor-name'),
#     # path('patient/',PatientViewSet.as_view(), name='patient-name'),
#     # path('appointment/',AppointmentViewSet.as_view(),  name='appointment'),
#     # path("prescription/",PrescriptionViewSet.as_view(),name="prescription"),
#     # path('medicalrecord/', MedicalRecordViewSet.as_view(), name='medicalrecord'),
#     # path('payment/<int:id>/', PaymentViewSet.as_view(), name='payment'),
#     # path('videocall/<int:id>/', VideoCallLogViewSet.as_view(), name='videocall'),
#     # path('feedback/', FeedbackViewset.as_view(), name='feedback'),
# ]
urlpatterns = [
    path('doctors-signup/', DoctorRegisterViewSet.as_view(), name='project-create'),
    path('doctors-login/',DoctorLoginViewSet.as_view(), name='doctor-login'),
    path('patient-signup/',PatientRegisterViewSet.as_view(), name='patient-create'),
    path('patient-login/',PatientLoginViewSet.as_view(), name='patient-create'),
    path('patient-sonar/',PatientLoginViewSet.as_view(), name='sonar-create'),
    path('patient-sonar-newB/',PatientLoginViewSet.as_view(), name='sonar-create-newB'),
    path('patient-sonar-newB1/',PatientLoginViewSet.as_view(), name='sonar-create-newB-monday1'),
    path('patient-sonar-newB2/',PatientLoginViewSet.as_view(), name='sonar-create-newB-monday2'),
    path('patient-sonar-newB3/',PatientLoginViewSet.as_view(), name='sonar-create-newB-monday3'),
#     # path('appointment/',AppointmentViewSet.as_view(),  name='appointment'),
#     # path("prescription/",PrescriptionViewSet.as_view(),name="prescription"),
#     # path('medicalrecord/', MedicalRecordViewSet.as_view(), name='medicalrecord'),
#     # path('payment/<int:id>/', PaymentViewSet.as_view(), name='payment'),
#     # path('videocall/<int:id>/', VideoCallLogViewSet.as_view(), name='videocall'),
#     # path('feedback/', FeedbackViewset.as_view(), name='feedback'),
]