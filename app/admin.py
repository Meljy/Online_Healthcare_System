from django.contrib import admin
from .models import Patient, Doctor, EmergencyCall  

admin.site.register(Patient)
admin.site.register(EmergencyCall) 

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'contact_number']
    search_fields = ['name', 'specialization', 'email']