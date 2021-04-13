from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
  return TemplateResponse(request,'index.html')

# Create your views here.

http://127.0.0.1:8000/