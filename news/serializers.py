from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def update(self, instance, validated_data):
        print('wtf')
        instance.title = validated_data.get("title", instance.title)
        instance.text = validated_data.get("text", instance.text)
        if validated_data.get("image"):
            instance.image = validated_data.get("image", instance.image)
        instance.save()