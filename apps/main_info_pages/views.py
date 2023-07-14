from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def aboutme(request):
    template = loader.get_template('aboutme.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())


def portfolio(request):
    template = loader.get_template('portfolio.html')
    return HttpResponse(template.render())


def layout(request):
    template = loader.get_template('layout.html')
    return HttpResponse(template.render())
