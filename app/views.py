from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Patient, Doctor, EmergencyCall
from accounts.models import CustomUser 

class DoctorFilterForm(forms.Form):
    specialization = forms.ChoiceField(required=False)
    search = forms.CharField(required=False)
    sort = forms.ChoiceField(
        choices=[
            ('name', 'Name (A-Z)'),
            ('-name', 'Name (Z-A)'),
            ('specialization', 'Specialization (A-Z)'),
            ('-specialization', 'Specialization (Z-A)')
        ],
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get unique specializations from the database
        specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
        spec_choices = [('', 'All Specializations')] + [(spec, spec) for spec in specializations]
        self.fields['specialization'].choices = spec_choices

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactUsView(TemplateView):
    template_name = 'app/contactus.html'

class DoctorsListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'app/doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DoctorFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Doctor.objects.all()
        
        # Get filter parameters from GET request
        specialization = self.request.GET.get('specialization')
        search = self.request.GET.get('search')
        sort = self.request.GET.get('sort')

        # Apply filters
        if specialization:
            queryset = queryset.filter(specialization=specialization)
        
        if search:
            queryset = queryset.filter(
                models.Q(name__icontains=search) |
                models.Q(specialization__icontains=search) |
                models.Q(email__icontains=search)
            )

        # Apply sorting
        if sort:
            queryset = queryset.order_by(sort)
        else:
            queryset = queryset.order_by('name')

        return queryset

class EmergencyView(TemplateView):
    template_name = 'app/emergency.html'
    
    def post(self, request, *args, **kwargs):
        location = request.POST.get('emergencyLocation')
        message = None
        
        if location:
            EmergencyCall.objects.create(location=location)
            message = f"🚑 Ambulance called to: {location}! Help is on the way!"
        else:
            message = "⚠️ Please provide a location!"
        
        return render(request, self.template_name, {'message': message})

class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'app/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'app/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'user', 'email', 'phone_number', 'date_of_birth', 'address', 'medical_history']
    template_name = 'app/patient_create.html'
    success_url = reverse_lazy('patient')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()  # Use CustomUser instead of User
        return context

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'user', 'email', 'phone_number', 'date_of_birth', 'address', 'medical_history']
    template_name = 'app/patient_update.html'
    success_url = reverse_lazy('patient')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'app/patient_delete.html'
    success_url = reverse_lazy('patient')