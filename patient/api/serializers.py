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
class PatientProfileCreateUpdateSerializer(ModelSerializer):
    patient    = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = PatientProfile
        fields = [
            'patient',
            'role',
            'years',
            'qualification1',
            'qualification2',
            'qualification3',
            'rating',
            'description',
            'latitude',
            'longitude',
        ]


patient_detail_url = HyperlinkedIdentityField(
        view_name='patient-api:detail',
        lookup_field='id'#or primary key <pk>
    )

# PatientProfile Details
class PatientProfileDetailSerializer(ModelSerializer):
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
            'role',
            'years',
            'qualification1',
            'qualification2',
            'qualification3',
            'rating',
            'description',
            'latitude',
            'longitude',
            'timestamp',
            'updated',
            'delete_url', 
        ]
    
# All PatientProfiles List
class PatientProfileListSerializer(ModelSerializer):
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
            'role',
            'years',
            'qualification1',
            'qualification2',
            'qualification3',
            'rating',
            'description',
            'latitude',
            'longitude',
            'timestamp',
            'updated',
            'delete_url', 
        ]