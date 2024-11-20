
# Create your views here.
from django.shortcuts import render,redirect
from . import forms


def add_category(request):
    if request.method == "POST":
         display_form=forms.Categoryform(request.POST)
         if display_form.is_valid():
              display_form.save()
              return redirect('add_category')
    else:
          display_form=forms.Categoryform()
    return render (request,'index.html',{'form': display_form})
