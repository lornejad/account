from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('last_name', 'is_staff', 'is_active',)
    list_filter = ('last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'medical_record', 'ECG', 'password1', 'password2', 'is_staff',
                       'is_active', 'last_login', 'date_joined', 'is_superuser')}
         ),
    )
    search_fields = ('last_name',)
    ordering = ('last_name',)


admin.site.register(CustomUser, CustomUserAdmin)
