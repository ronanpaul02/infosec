from django.shortcuts import render

# Create your views here.


def home(request):
    #comment
    return render(request, 'home.html')
