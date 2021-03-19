from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.serializers import (
    CharField, 
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    HiddenField,
    CurrentUserDefault
    )


User = get_user_model()

#User Details
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'first_name',
            'last_name', 
            'gender',
            'address',
            'dob',
            'phone_number',
            'next_of_kin',
            'id',
        ]


#user Login
class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    # username = CharField()
    user = UserDetailSerializer(read_only=True)
    email = EmailField(label='Email Address', required=True, allow_blank=False)
    class Meta:
        model = User
        fields = [
            # 'username',
            'email',
            'password',
            'token',
            'user',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            } 
    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        # username = data.get("username", None)
        password = data["password"]
        if not email:
            raise ValidationError("A Email is required to login.")

        user = User.objects.filter(
                Q(email=email)
        ).distinct()
        # user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This useEmailrname is not valid.")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        data["token"] = "SOME RANDOM TOKEN"
        return data

#Create Album
class UserCreateSerializer(ModelSerializer):
    email = EmailField(label = 'Email Address')
    next_of_kin = CharField(label = 'Next of Kin Phone number')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name', 
            'email',
            'password',
            'gender',
            'address',
            'dob',
            'phone_number',
            'next_of_kin',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data