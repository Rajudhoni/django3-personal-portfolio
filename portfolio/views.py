from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    project = Project.objects.order_by('-id')
    return render(request, 'portfolio/home.html', {'projects':project})