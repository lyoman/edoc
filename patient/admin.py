from django.contrib import admin
from .models import PatientProfile

# Register your models here.
class PatientProfileModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "patient", 'location', "latitude", "longitude", "updated", "timestamp"]
    list_display_links  = ["updated", "timestamp"]
    list_editable		= ["latitude", "longitude"]
    list_filter			= ["patient", "updated", "timestamp", "location"]
    search_fields		= ["location", "user__username"]
    class Meta:
        model = PatientProfile
  
admin.site.register(PatientProfile, PatientProfileModelAdmin)