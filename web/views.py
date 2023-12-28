from django.http import HttpResponse
from django.shortcuts import render

from web.models import Example


def home(request) -> HttpResponse:
    examples = Example.objects.all()

    context = {
        "examples": examples
    }
    return render(request, "web/home.html", context=context)
