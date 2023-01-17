from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from app.forms import *

def fbv_string(request):
    return HttpResponse('<h1>i am return httpresponse from fbv_string</h2>')

def fbv_page(request):
    return render(request,"fbv_page.html")

class Cbv_String(View):
    def get(self,request):
        return HttpResponse('i am using cbv string')

class Cbv_page(View):
    def get(self,request):
        return render(request,"cbv_page.html")

def fbv(request):
    form=StudentForm()
    d={'form':form}
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,"fbv.html",d)

class Cbv(View):
    def get(self,request):
        form=StudentForm()
        d={'form':form}
        return render(request,'cbv.html',d)

    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

