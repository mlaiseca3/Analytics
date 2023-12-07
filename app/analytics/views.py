# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render

from .serializers import HeroSerializer
from .models import Hero

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You are in the analytics app index.")


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

def front(request):
    context = {}
    return render(request, "index.html", context)
