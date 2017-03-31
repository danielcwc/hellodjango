from rest_framework import serializers
from books.models import *

class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField(required=False)

    # it can be called directly to create an object instance
    # it's also called in super.save() if super.instance is None
    def create(self, validated_data):
        return Author(**validated_data)


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=60)
    state_province = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=50)
    website = serializers.URLField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    publication_date = serializers.DateField(required=False)
