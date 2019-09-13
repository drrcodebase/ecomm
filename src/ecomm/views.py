from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
def home_page(request):
    context = {
        "title":"Welcome To E-Commerce World",
        "content" : "Welcome to the Home Page",
        "premium_content": "YEAHHHHHHHHHHHH"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):

    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact  Page",
        "content":"welcome to the content page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you"})
    if contact_form.errors:
        print(contact_form.cleaned_data)
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    return render(request, "contact/view_page.html", context)
