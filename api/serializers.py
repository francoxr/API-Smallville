from rest_framework import serializers
from .models import Author, Quotes


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author 
        fields = '__all__'
    

class QuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotes
        fields = '__all__'


class QuotesGetSerializer(serializers.ModelSerializer):

    author_id = AuthorSerializer()

    class Meta:
        model = Quotes
        fields = ['content', 'author_id']