from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import RecipeSerializer
from .models import Recipe

# Create your views here.
def index(request):
    return HttpResponse("Test")

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
