from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.utils import timezone


class UserSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserSite
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CustomUser
        exclude = ['password']

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.is_superuser = validated_data.get("is_superuser", instance.is_superuser)
        instance.is_staff = validated_data.get("is_superuser", instance.is_superuser)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        site_id = validated_data.pop('site')
        if site_id:
            site = CustomUserSite.objects.get(id=site_id)
            instance.site = site
        instance.save()


class RegistrationSerializer(serializers.ModelSerializer):
    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    comment = serializers.CharField(write_only=True, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField(write_only=True)
    is_staff = serializers.BooleanField(write_only=True)
    site = serializers.IntegerField(write_only=True, allow_null=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        site_id = validated_data.pop('site')
        if site_id:
            site = CustomUserSite.objects.get(id=site_id)
            validated_data['site'] = site
        if validated_data.get('is_staff', False):
            return CustomUser.objects.create_superuser(**validated_data)
        else:
            return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Authenticates an existing user.
    Email and password are required.
    Returns a JSON web token.
    """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    token = serializers.CharField(max_length=255, read_only=True)
    amount = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)
        user.last_visit = timezone.now()
        user.save()

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        if not user.is_staff:
            raise serializers.ValidationError(
                'У данного пользователя нет прав доступа к админ панели'
            )

        return {
            'token': user.token,
            'email': user.email,
            'amount': user.amount
        }