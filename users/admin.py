from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    list_display 	    = ["id", "username", "email", 'gender', "city", "phone_number", "address", "next_of_kin",  "is_patient", "is_doctor", "is_nurse", "is_active", "is_staff", "is_superuser", "updated", "timestamp"]
    list_display_links  = ["updated", "username"]
    list_editable		= ["is_active"]
    list_filter			= ["is_doctor", "is_nurse", "is_patient", "is_staff", "is_superuser", "updated", "timestamp", "email"]
    search_fields		= ["username", "email"]
    class Meta:
        model = User
  
admin.site.register(User, UserModelAdmin)