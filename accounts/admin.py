from django.contrib import admin
# from crimeA.models import CrimeReport
# from django.contrib.auth.models import User
# Register your models here.

# Register the CrimeReport model to the admin interface
# class CrimeReportAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'location', 'date_reported', 'reporter')
#     list_filter = ('category', 'date_reported')
#     search_fields = ('title', 'description', 'location')
#
# admin.site.register(CrimeReport, CrimeReportAdmin)

# Customize the User model in the admin interface
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
#     list_filter = ('is_staff', 'is_active')
#     search_fields = ('username', 'email')

  # Unregister the default User model
#admin.site.register(User, UserAdmin)  # Register the custom User model admin