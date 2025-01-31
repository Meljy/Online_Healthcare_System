from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
class EmergencyCall(models.Model):  # new model emergencycall
    location = models.CharField(max_length=200)
    called_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Emergency at {self.location} ({self.called_at})"

# existing models 
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Fixing the __str__ method

    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"pk": self.pk})


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"Dr. {self.name}"