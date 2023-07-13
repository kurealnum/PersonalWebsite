from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def aboutme(request):
    template = loader.get_template('layout.html')
    return HttpResponse(template.render())
