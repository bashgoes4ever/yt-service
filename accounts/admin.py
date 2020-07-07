from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from plans.admin import CustomPlanPricesInline


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'comment', 'amount', 'date_joined', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Информация', {'fields': ('comment', 'amount', 'date_joined', 'site', 'api_token', 'a_field', 'last_visit')}),
        ('Доступы', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'comment', 'amount', 'site', 'api_token', 'a_field', 'last_visit')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = [CustomPlanPricesInline]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserSite)