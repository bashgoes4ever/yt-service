from rest_framework import serializers
from .models import *
from accounts.models import CustomUser


class PlanSerializer(serializers.ModelSerializer):
    provider_id = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'provider_id']

    def create(self, validated_data):
        return Plan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.provider_id = validated_data.get("provider_id", instance.provider_id)
        instance.save()


class CustomPricesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = CustomPlanPrices
        fields = ['id', 'min_amount', 'max_amount', 'price', 'user', 'plan']

    def create(self, validated_data):
        price_id = validated_data.pop('id', False)
        if price_id:
            plan, created = CustomPlanPrices.objects.update_or_create(id=price_id, defaults=validated_data)
        else:
            plan = CustomPlanPrices.objects.create(**validated_data)
        return plan
