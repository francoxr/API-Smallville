from rest_framework import serializers
from .models import Author, Quotes

class QuotesSerializer(serializers.ModelSerializer):

    # def __init__(self, instance=None, data=empty, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(QuotesSerializer, self).__init__(instance=None, data=empty, **kwargs)

    class Meta:
        model = Quotes
        fields = '__all__'
        # fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    # quote_id = QuotesSerializer(read_only=True, many=True)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(AuthorSerializer, self).__init__(many=many, *args, **kwargs)
    
    class Meta:
        model = Author 
        # add all fields
        fields = '__all__'
        # get nested data
        # depth = 1

    
    # def get_type_ids(self, obj):

    #     type_ids = Types.objects.order_by('-id')
    #     return TypesSerializer(type_ids, read_only=True, many=True, context=self.context)