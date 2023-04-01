from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  people =[
    {"name":"Pritam","age":26},
    {"name":"Adrija","age":27},
          ]
  return render(request, "index.html",context={'peoples':people})


def success_page(request):
    return HttpResponse("HI from success")
