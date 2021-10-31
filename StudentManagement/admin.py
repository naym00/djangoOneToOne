from django.contrib import admin
from .models import Student, RegistrationID
# Register your models here.

admin.site.register([Student, RegistrationID])