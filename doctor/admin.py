from django.contrib import admin
from .models import DoctorRole

# Register your models here.
class DoctorRoleModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "doctor", "role", 'description', "updated", "timestamp"]
    list_display_links  = ["updated", "role"]
    # list_editable		= []
    list_filter			= ["doctor", "updated", "timestamp"]
    search_fields		= ["description", "role"]
    class Meta:
        model = DoctorRole
  
admin.site.register(DoctorRole, DoctorRoleModelAdmin)