from django.contrib import admin
from .models import DoctorRole

# Register your models here.
class DoctorRoleModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "doctor", "role", "years", "qualification1", "rating", 'description', "latitude", "longitude", "updated", "timestamp"]
    list_display_links  = ["updated", "role"]
    list_editable		= ["latitude", "longitude"]
    list_filter			= ["doctor", "updated", "timestamp", "years", "rating"]
    search_fields		= ["description", "role", "years", "rating"]
    class Meta:
        model = DoctorRole
  
admin.site.register(DoctorRole, DoctorRoleModelAdmin)