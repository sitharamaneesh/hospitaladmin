from django.contrib import admin

from .models import *


@admin.register(doctor, Inpatient,Outpatient,nurse,covid,stafflogin,medicalrecord,pharmacy,medicine,discharge)
class AppAdmin(admin.ModelAdmin):
    pass

    def __str__(self) :
        return self.list_display