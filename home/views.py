from django.shortcuts import render
from home.models import Contact
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request, "contact.html")