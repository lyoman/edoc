from django.db import models
from users.models import User

ROLE_CHOICES = (
    ("Neurology", "Neurology"),
    ("Urology", "Urology"),
    ("Cardiology", "Cardiology"),
    ("Dentist", "Dentist"),
    ("Optision", "Optision")
)
# Create your models here.
class DoctorRole(models.Model):
    doctor         = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    role           = models.CharField(max_length=200, blank=False, null=False,choices=ROLE_CHOICES)
    description    = models.CharField(max_length=200, blank=False, null=False)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.role
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
