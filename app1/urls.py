from django.urls import path
from app1.views import *
app_name='Anushka'

urlpatterns=[
    path('arundhathi/',arundhathi,name='arundhathi'),
]