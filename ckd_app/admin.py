from django.contrib import admin

# Register your models here.
from .models import Patient

admin.site.register(Patient)  # Registers the Patient model in Django Admin
