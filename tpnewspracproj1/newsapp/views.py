from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "newsapp/index.html")

def moviesnews(request):
    return render(request,"newsapp/bollynews.html")

def politicsnews(request):
    return render(request,"newsapp/politicsnews.html")

def sportsnews(request):
    return render(request,"newsapp/sportsnews.html")
