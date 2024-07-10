from django.urls import path
from .views import contact, contact_form

urlpatterns = [
    path('', contact, name='contact'),
    path('submit/', contact_form, name='contact_form'),
]