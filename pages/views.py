from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def homePage(request):
#     return HttpResponse('Are u ready for amazing apps')

class HomePage(TemplateView):
    template_name = 'pages/home.html'
    
class AboutPage(TemplateView): 
    template_name = 'pages/about.html'