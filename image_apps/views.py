from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import ListView


def images(requests):
    context = {
        "img1": "C:\\Users\\DELL\\PycharmProjects\\djangoAssignment\\templates\\images\\1.jpg"
    }
    return render(requests, "BaseHome.html", context)
