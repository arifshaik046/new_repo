from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import View
from .models import login_table
# Create your views here.
def hello(request):
    return HttpResponse('hello world')

class login_page(View):
    def get(self,request):
        print("login page")
        tmplt = loader.get_template('login.html')
        return HttpResponse(tmplt.render({},request))

class add_records(View):
    def post(self,request):
        name = request.POST.get('name')
        pasw = request.POST.get('password')
        tmplt = loader.get_template('table.html')
        mdl = login_table(name=name,password=pasw)
        # mdl.save()
        values = login_table.objects.all().values()
        print(values)
        context={'data':values}
        return HttpResponse(tmplt.render(context,request))
    # return HttpResponseRedirect(reverse(''))
# def login_page(request):
#     print("login page")
#     tmplt = loader.get_template('login.html')
#     return HttpResponse(tmplt.render({},request))

# def add_records(request):
    
#     name = request.POST.get('name')
#     pasw = request.POST.get('password')
#     mdl = login_table(name=name,password=pasw)
#     mdl.save()
#     values = login_table.objects.all().values()
#     return HttpResponse(values)
    # return HttpResponseRedirect(reverse(''))