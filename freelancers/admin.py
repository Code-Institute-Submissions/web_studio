from django.contrib import admin

from .models import Freelancer


# for the date field to be visible in Admin panel
# https://stackoverflow.com/a/23660030
class FreelancerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(Freelancer, FreelancerAdmin)
