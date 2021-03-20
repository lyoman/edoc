from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
    PatientCreateAPIView,
    PatientListAPIView,
    PatientDetailAPIView,
    PatientUpdateAPIView,
    PatientDeleteAPIView,
	)

urlpatterns = [
    path('', PatientListAPIView.as_view(), name='patients'),
    path('create/', PatientCreateAPIView.as_view(), name="addpatient"),
    path('<int:id>/', PatientDetailAPIView.as_view(), name='detail'),
    path('<int:id>/delete/', PatientDeleteAPIView.as_view(), name="delete"),
    path('<int:id>/edit/', PatientUpdateAPIView.as_view(), name='update'),
]