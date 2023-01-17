from django.shortcuts import render
from rest_framework import generics
from .serializers import JokeSerializer
from .models import Joke

# Create your views here.
class JokeList(generics.ListCreateAPIView):
    queryset = Joke.objects.all().order_by('id')
    serializer_class = JokeSerializer

class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all().order_by('id')
    serializer_class = JokeSerializer