from django.contrib import admin

from .models import Order

# for the date field to be visible in Admin panel
# https://stackoverflow.com/a/23660030
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Order,OrderAdmin)
