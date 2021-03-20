from django.contrib import admin
from .models import PatientProfile

# Register your models here.
class PatientProfileModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "doctor", "role", "years", "qualification1", "rating", 'description', "latitude", "longitude", "updated", "timestamp"]
    list_display_links  = ["updated", "role"]
    list_editable		= ["latitude", "longitude"]
    list_filter			= ["doctor", "updated", "timestamp", "years", "rating"]
    search_fields		= ["description", "role", "years", "rating"]
    class Meta:
        model = PatientProfile
  
admin.site.register(PatientProfile, PatientProfileModelAdmin)