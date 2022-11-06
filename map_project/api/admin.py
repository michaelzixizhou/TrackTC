from django.contrib import admin
from .models import TTCUser
from django.contrib.auth.admin import UserAdmin
from typing import Optional

admin.site.register(TTCUser)
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields':(
                    'favourites'
                )
            }
        )
    )