from django.contrib import admin

from .models import Appointment


# for the date field to be visible in Admin panel
# https://stackoverflow.com/a/23660030
class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Appointment, AppointmentAdmin)
