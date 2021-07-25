from django.urls import path

from . views import *

urlpatterns = [
    path('', index, name="index"),
    path('details/<int:pk>', details, name="details" )
]
