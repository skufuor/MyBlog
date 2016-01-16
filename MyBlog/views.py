from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home_page(request):
    return HttpResponse("This is my Blog.")

def about_me(request):
    return HttpResponse("About Me!!!")

def page(request, page_name):
    output_str = "A specfic page: " + page_name    
    return HttpResponse(output_str)

def newest_page(request):
    return HttpResponse("This is my newest blog post")
