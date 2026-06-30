from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome to Barofchocolate fun\'s website </h1>')

def contact(request):
    return HttpResponse('contact Barofchocolate fun here')

def about(request):
    return HttpResponse('Barofchocolate fun is the best fun center you can in Africa and Europe')

