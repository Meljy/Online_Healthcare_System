from django.urls import path
from .views import (
    HomePageView, AboutPageView, PatientListView,
    PatientDetailView, PatientCreateView, PatientUpdateView,
    PatientDeleteView, ContactUsView, DoctorsListView,
    EmergencyView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('doctors/', DoctorsListView.as_view(), name='doctors'),
    path('emergency/', EmergencyView.as_view(), name='emergency'),
    path('patient/', PatientListView.as_view(), name='patient'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]