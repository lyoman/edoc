from django.db import models
from users.models import User

# ROLE_CHOICES = (
#     ("Neurology", "Neurology"),
#     ("Urology", "Urology"),
#     ("Cardiology", "Cardiology"),
#     ("Dentist", "Dentist"),
#     ("Optision", "Optision")
# )
# Create your models here.
class PatientProfile(models.Model):
    patient         = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    role           = models.CharField(max_length=200, blank=False, null=False)
    years          = models.CharField(max_length=200, blank=True, null=True)
    qualification1 = models.CharField(max_length=200, blank=True, null=True)
    qualification2 = models.CharField(max_length=200, blank=True, null=True)
    qualification3 = models.CharField(max_length=200, blank=True, null=True)
    rating         = models.CharField(max_length=200, blank=True, null=True)
    description    = models.CharField(max_length=200, blank=False, null=False)
    latitude	   = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    longitude	   = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.role
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
