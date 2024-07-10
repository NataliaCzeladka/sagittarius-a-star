from django.contrib import admin
from .models import ContactFormRequest


@admin.register(ContactFormRequest)
class ContactFormRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message', 'date_sent')
    list_filter = ('date_sent')
    search_fields = ('name', 'email', 'message')
