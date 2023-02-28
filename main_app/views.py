from django.shortcuts import render

finches = [
  {'name': 'Zulu', 'type': 'Cassia Crossbill', 'description': 'will fight birds for seeds', 'age': 2},
  {'name': 'Thomas', 'type': 'Indigo Bunting', 'description': 'likes to bring humans sticks', 'age': 1},
]

# Create your views here.
# Define the home view
def home(request):
    #include an .html file extension - ublike when rendering EJS Templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })