from django.contrib import admin
from .models import *


class CustomPlanPricesInline(admin.TabularInline):
    model = CustomPlanPrices
    extra = 0


class CustomPlanPricesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomPlanPrices._meta.fields]

    class Meta:
        model = CustomPlanPrices


class PlanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Plan._meta.fields]
    inlines = [CustomPlanPricesInline]

    class Meta:
        model = Plan


admin.site.register(CustomPlanPrices, CustomPlanPricesAdmin)
admin.site.register(Plan, PlanAdmin)
