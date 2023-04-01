from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  people =[
    {"name":"Pritam","age":26},
    {"name":"Adrija","age":27},
          ]
  text="If you did not attempt to sign in to your account, your password may be compromised. Visit https://github.com/settings/security to create a new, strong password for your GitHub account,If you'd like to automatically verify devices in the future, consider enabling two-factor authentication on your account"
  vegetables=["Pumpkin","tomato","potato"]
  return render(request, "index.html",context={'peoples':people,"text":text,"vegetables":vegetables})


def success_page(request):
    return HttpResponse("HI from success")
