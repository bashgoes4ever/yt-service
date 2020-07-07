from rest_framework import serializers
from .models import *
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email']


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        depth=1


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        account = validated_data.get("user")
        total_price = validated_data.get("plan").price * validated_data.get("amount")
        price = validated_data.get("plan").price
        if account.customplanprices_set.exists():
            for range in account.customplanprices_set.all():
                if range.min_amount <= validated_data.get("amount") <= range.max_amount:
                    price = range.price
                    total_price = price * validated_data.get("amount")
                    break
        if (account.amount - total_price) >= 0:
            account.amount = account.amount - total_price
            account.save()
            validated_data['total_price'] = total_price
            validated_data['price'] = price
            return Order.objects.create(**validated_data)
        raise serializers.ValidationError('На счету недостаточно средств')

    def update(self, instance, validated_data):
        instance.price = validated_data.get("price", instance.price)
        instance.provider_id = validated_data.get("provider_id", instance.provider_id)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.remains = validated_data.get("remains", instance.remains)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.plan = Plan.objects.get(id=validated_data.get("plan", instance.plan))
        instance.status = OrderStatus.objects.get(id=validated_data.get("status", instance.status))
        instance.save()


class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        account = validated_data.get("user")
        total_price = validated_data.get("plan").price * validated_data.get("amount")
        price = validated_data.get("plan").price
        if account.customplanprices_set.exists():
            for range in account.customplanprices_set.filter(plan=validated_data.get("plan")):
                if range.min_amount <= validated_data.get("amount") <= range.max_amount:
                    price = range.price
                    total_price = price * validated_data.get("amount")
                    break
        if (account.amount - total_price) >= 0:
            account.amount = account.amount - total_price
            account.save()
            validated_data['total_price'] = total_price
            validated_data['price'] = price
            return Order.objects.create(**validated_data)
        raise serializers.ValidationError('На счету недостаточно средств')
