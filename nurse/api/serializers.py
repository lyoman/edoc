from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from nurse.models import NurseProfile
from users.api.serializers import UserDetailSerializer
from django.contrib.auth.models import User
from django.db import models

#Creating a NurseProfile
class NurseProfileCreateUpdateSerializer(ModelSerializer):
    nurse    = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    class Meta:
        model = NurseProfile
        fields = [
            'nurse',
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


nurse_detail_url = HyperlinkedIdentityField(
        view_name='nurse-api:detail',
        lookup_field='id'#or primary key <pk>
    )

# NurseProfile Details
class NurseProfileDetailSerializer(ModelSerializer):
    url         = nurse_detail_url
    nurse      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='nurse-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = NurseProfile
        fields = [
            'url',
            'id',
            'nurse',
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
    
# All NurseProfiles List
class NurseProfileListSerializer(ModelSerializer):
    url         = nurse_detail_url
    nurse      = UserDetailSerializer(read_only=True)
    delete_url  = HyperlinkedIdentityField(
        view_name='nurse-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = NurseProfile
        fields = [
            'url',
            'nurse',
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