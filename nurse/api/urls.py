from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
    NurseCreateAPIView,
    NurseListAPIView,
    NurseDetailAPIView,
    NurseUpdateAPIView,
    NurseDeleteAPIView,
	)

urlpatterns = [
    path('', NurseListAPIView.as_view(), name='nurses'),
    path('create/', NurseCreateAPIView.as_view(), name="addnurse"),
    path('<int:id>/', NurseDetailAPIView.as_view(), name='detail'),
    path('<int:id>/delete/', NurseDeleteAPIView.as_view(), name="delete"),
    path('<int:id>/edit/', NurseUpdateAPIView.as_view(), name='update'),
]