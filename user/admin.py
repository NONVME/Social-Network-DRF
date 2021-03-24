from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SiteUser

admin.site.register(SiteUser, UserAdmin)
