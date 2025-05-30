from django.shortcuts import render

# Create your views here.


# pages/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'pages/page.html')
