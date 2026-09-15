from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import ContactForm


def home(request):
    return HttpResponse("Привет мир !")


def contact_view(request):
    form = ContactForm()

    contex = {"form": form}
    return render(request, "blog/contact.html", contex)
