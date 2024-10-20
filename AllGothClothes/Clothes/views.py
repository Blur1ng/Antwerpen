from typing import Any
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import auth
from .utils import *
from .models import *
import os
from django.views.decorators.csrf import csrf_exempt

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
        abspath4images = '/Users/evgene/Documents/django/djsite2/AllGothClothes/AllGothClothes/Clothes/static/Clothes/images/4body'
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Brands page')
        super_dict = dict(list(context.items()) + list(c_def.items()))
        super_dict["images"] = [f for f in os.listdir(abspath4images) if os.path.isfile(os.path.join(abspath4images, f))]
        return super_dict
    
class Conjunctiva(Allbrandssettings):
    template_name = "brands/Conjunctiva.html"   
class Convulsive(Allbrandssettings):
    template_name = "brands/Convulsive.html"
class HikikomoriKai(Allbrandssettings):
    template_name = "brands/hikikomori Kai.html"
class Iseedeadpeople(Allbrandssettings):
    template_name = "brands/Iseedeadpeople.html"   

class Cloth_detail(DataMixin, ListView):
    template_name = "Clothes/detail.html"
    model = Cloth
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        accurate_rating = Cloth.objects.get(name=self.kwargs['cloth_name'])
        context = super().get_context_data(**kwargs)
        context['brand_name'] = self.kwargs['brand_name']
        context['cloth_name'] = self.kwargs['cloth_name']
        context['rating'] = round(accurate_rating.rating / accurate_rating.count_of_votes, 1)
        c_def = self.get_user_context(title=self.kwargs['cloth_name'])
        return dict(list(context.items()) + list(c_def.items()))  
      
class Feedback(Allbrandssettings):
    template_name = "Clothes/feedback.html"   

class News(Allbrandssettings):
    template_name = "Clothes/news.html"   

def rate_cloth(request):
    if request.method == 'POST':
        cloth_name = request.POST.get('cloth_name')
        rating = int(request.POST.get('rating'))
        
        try:                 
            cloth = Cloth.objects.get(name=cloth_name)
            # Проверяем, существует ли уже голос от пользователя
            vote, created = Vote.objects.get_or_create(cloth=cloth, user=request.user)

            if not created:
                # Обновляем существующую оценку
                old_rating = vote.old_rating 
                vote.save()
                
                end_rate = round((cloth.rating - old_rating + rating) / cloth.count_of_votes, 1)
                cloth.rating = cloth.rating - old_rating + rating
                vote.old_rating = rating
                vote.save()
            else:
                # Новый голос
                cloth.count_of_votes += 1
                end_rate = round((cloth.rating + rating) / cloth.count_of_votes, 1)
                cloth.rating = cloth.rating + rating 
                vote.old_rating = rating 
                vote.save()

            cloth.save()
            return JsonResponse({'status': 'success', 'new_rating': end_rate})

        except Cloth.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cloth not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

