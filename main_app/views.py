from django.shortcuts import render
# Importing the Finch Model from models.py
from .models import Finch

# Create your views here.1
# Define the home view
def home(request):
    #include an .html file extension - ublike when rendering EJS Templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })