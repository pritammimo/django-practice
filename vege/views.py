from django.shortcuts import render
from .models import *
# Create your views here.
def receipes(request):
  if request.method == "POST":
    data=request.POST
    receipe_name=data.get("receipe_name")
    receipe_description=data.get("receipe_description")
    receipe_image=request.FILES.get("receipe_image")
    Receipe.objects.create(
      receipe_name=receipe_name,
      receipe_image=receipe_image,
      receipe_description=receipe_description
    )
    print(receipe_name)
    print(receipe_image)
    print(receipe_description)
  return render(request,'receipes.html')