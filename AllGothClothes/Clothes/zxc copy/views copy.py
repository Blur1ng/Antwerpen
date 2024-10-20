from typing import Any
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import ImproperlyConfigured
from django.template.response import TemplateResponse
from .utils import *
from .models import *

class Mainpage(DataMixin, ListView):
    template_name = "Clothes/index.html"
    model = Cloth
    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(c_def.items()))

class Brands(DataMixin, ListView):
    template_name = "Clothes/brands.html"
    model = Brand
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Brands page')
        return dict(list(context.items()) + list(c_def.items()))

class Conjunctiva(Allbrandssettings):
    template_name = "brands/Conjunctiva.html"   
class Convulsive(Allbrandssettings):
    template_name = "brands/Convulsive.html"
class HikikomoriKai(Allbrandssettings):
    template_name = "brands/hikikomori Kai.html"
class Iseedeadpeople(Allbrandssettings):
    template_name = "brands/Iseedeadpeople.html"   

def indexItem(request, id):
    item = Cloth.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "Clothes/detail.html", context=context)

def Feedback(reverse):
    return HttpResponse('Feedback')

def Backstage(reverse):
    return HttpResponse('Backstage')