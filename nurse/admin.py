from django.contrib import admin
from .models import NurseProfile

# Register your models here.
class NurseProfileModelAdmin(admin.ModelAdmin):
    list_display 	    = ["id", "nurse", "role", "years", "qualification1", "rating", 'description', "latitude", "longitude", "updated", "timestamp"]
    list_display_links  = ["updated", "role"]
    list_editable		= ["latitude", "longitude"]
    list_filter			= ["nurse", "updated", "timestamp", "years", "rating"]
    search_fields		= ["description", "role", "years", "rating"]
    class Meta:
        model = NurseProfile
  
admin.site.register(NurseProfile, NurseProfileModelAdmin)