# landing/urls.py
from django.urls import path
from .views import inquiry_view, contact_button_view, contact_click

urlpatterns = [
    path('inquire/', inquiry_view, name='inquire'),
    path('', contact_button_view, name='contact'),
    path('contact-click/', contact_click, name='contact-click'),
]