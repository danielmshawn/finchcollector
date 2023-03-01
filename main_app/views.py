from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'
