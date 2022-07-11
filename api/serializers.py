from dataclasses import fields
from http import server
from .models import Article
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Article
            fields = '__all__' 
        
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=400)

    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #    instance.title = validated_data.get('title', instance.title)
    #    instance.description = validated_data.get('description', instance.description)


