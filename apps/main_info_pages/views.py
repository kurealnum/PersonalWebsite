from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def aboutme(request):
    template = loader.get_template('aboutme.html')
    return HttpResponse(template.render())


def layout(request):
    #basic variables
    template = loader.get_template('layout.html')
    referer_url = request.META.get('HTTP_REFERER')

    #if we're coming from "/", just
    if not referer_url:
        return redirect("index")

    return HttpResponse(template.render())
