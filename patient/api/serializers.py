from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from patient.models import PatientProfile
from users.api.serializers import UserDetailSerializer
from django.contrib.auth.models import User
from django.db import models

#Creating a PatientProfile
class PatientCreateUpdateSerializer(ModelSerializer):
    patient    = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = PatientProfile
        fields = [
            'patient',
            'location',
            'latitude',
            'longitude',
            'latitude',
            'longitude',
        ]


patient_detail_url = HyperlinkedIdentityField(
        view_name='patient-api:detail',
        lookup_field='id'#or primary key <pk>
    )

# PatientProfile Details
class PatientDetailSerializer(ModelSerializer):
    url         = patient_detail_url
    patient      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='patient-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = PatientProfile
        fields = [
            'url',
            'id',
            'patient',
            'location',
            'latitude',
            'longitude',
            'timestamp',
            'updated',
            'delete_url', 
        ]
    
# All PatientProfiles List
class PatientListSerializer(ModelSerializer):
    url         = patient_detail_url
    patient      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='patient-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = PatientProfile
        fields = [
            'url',
            'patient',
            'id',
            'location',
            'latitude',
            'longitude',
            'timestamp',
            'updated',
            'delete_url', 
        ]