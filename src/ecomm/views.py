from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title":"Hello world title"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    context = {
        "title":"contact  Page"
    }
    return render(request, "home_page.html", context)
