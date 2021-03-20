from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from doctor.models import DoctorRole
from users.api.serializers import UserDetailSerializer
from django.contrib.auth.models import User
from django.db import models

#Creating a DoctorRole
class DoctorRoleCreateUpdateSerializer(ModelSerializer):
    doctor    = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = DoctorRole
        fields = [
            'doctor',
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


doctor_detail_url = HyperlinkedIdentityField(
        view_name='doctor-api:detail',
        lookup_field='id'#or primary key <pk>
    )

# DoctorRole Details
class DoctorRoleDetailSerializer(ModelSerializer):
    url         = doctor_detail_url
    doctor      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='doctor-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = DoctorRole
        fields = [
            'url',
            'id',
            'doctor',
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
    
# All DoctorRoles List
class DoctorRoleListSerializer(ModelSerializer):
    url         = doctor_detail_url
    doctor      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='doctor-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = DoctorRole
        fields = [
            'url',
            'doctor',
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