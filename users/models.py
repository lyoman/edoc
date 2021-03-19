from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
)
# Create your models here.
class User(AbstractUser):
    is_hospital         = models.BooleanField(default=False)
    is_ambulance        = models.BooleanField(default=False)
    is_pharmacy         = models.BooleanField(default=False)
    is_nurse            = models.BooleanField(default=False)
    is_doctor           = models.BooleanField(default=False)
    is_patient          = models.BooleanField(default=False)
    gender              = models.CharField(max_length=200, blank=False, null=False,choices=GENDER_CHOICES)
    address             = models.TextField(blank=False, null=False)
    dob                 = models.DateField(null=True, blank=True)
    email               = models.EmailField(unique=True, blank=False)
    phone_regex         = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number        = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    next_of_kin         = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    updated             = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp           = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
