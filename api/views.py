from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Quotes
from .serializers import AuthorSerializer, QuotesSerializer, QuotesGetSerializer

from rest_framework import generics

# Create your views here.
def HelloWorld(request):
    return HttpResponse("hello SmallVille!")


class AuthorCreateAPIView(generics.CreateAPIView):
    """Api endpoint that allows create a Author object"""
    serializer_class = AuthorSerializer

class AuthorList(generics.ListAPIView):
    # API endpoint that allows Author to be viewed.
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorOneList(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class QuotesCreateApiView(generics.CreateAPIView):
    """Api endpoint that allow create a Quotes object"""
    serializer_class = QuotesSerializer

class QuotesList(generics.ListAPIView):
    # API endpoint that allows Quotes to be viewed.
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer

class QuotesOneList(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer

class QuotesOneListEspecial(generics.RetrieveAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuotesGetSerializer