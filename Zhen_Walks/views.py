from django.shortcuts import render, HttpResponse
from Zhen_Walks.models import Contact


# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        desc = request.POST["desc"]
        print(name, email, desc)

        data = Contact(name=name, email=email, desc=desc)
        data.save()

    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")
