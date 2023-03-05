from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Importing the Finch Model from models.py
from .models import Finch, Accessory
from .forms import FeedingForm

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
    # Get the accessories the finch doesn't have...
    # First, create a list of the accessory ids that the finch DOES have
    id_list = finch.accessories.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    accessories_finch_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    # Here we instantiate the FeedingForm class from forms.py which will render the form on the detail pg
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        # Add the accessories to be displayed
        'accessories': accessories_finch_doesnt_have
        })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

# @login_required
def assoc_accessory(request, finch_id, accessory_id):
  Finch.objects.get(id=finch_id).accessories.add(accessory_id)
  return redirect('detail', finch_id=finch_id)

# @login_required
def unassoc_accessory(request, finch_id, accessory_id):
  Finch.objects.get(id=finch_id).accessories.remove(accessory_id)
  return redirect('detail', finch_id=finch_id)