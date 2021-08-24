from django.http import HttpResponse
from django.shortcuts import render


def index():
    return HttpResponse('404 Page Not Found')
