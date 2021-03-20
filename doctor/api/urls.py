from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
    DoctorCreateAPIView,
    DoctorListAPIView,
    DoctorDetailAPIView,
    DoctorUpdateAPIView,
    DoctorDeleteAPIView,
	)

urlpatterns = [
    path('', DoctorListAPIView.as_view(), name='doctors'),
    path('create/', DoctorCreateAPIView.as_view(), name="adddoctor"),
    path('<int:id>/', DoctorDetailAPIView.as_view(), name='detail'),
    path('<int:id>/delete/', DoctorDeleteAPIView.as_view(), name="delete"),
    path('<int:id>/edit/', DoctorUpdateAPIView.as_view(), name='update'),
]