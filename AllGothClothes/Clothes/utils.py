from .models import *
from typing import Any
from django.views.generic import ListView

menu = [{'title': 'BRANDS', 'url_name': 'Brands'},
        {'title': 'FEEDBACK', 'url_name': 'Feedback'},
        {'title': 'NEWS', 'url_name': 'News'},
        {'title': 'LOGIN', 'url_name': 'login'},
]
class DataMixin:
    def get_user_context(self, **kwargs):       
        context = kwargs
        context["menu"] = menu
        return context
class Allbrandssettings(DataMixin, ListView):
    model = Cloth
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        brand_name = str(context["view"]).split()[0][15:]

        #---Распределение вещей по рядам---#          
        itemsf_ = []
        lst = []
        context["title"] = brand_name                    
        context["menu"] = menu
        globlal_i= 1
        for cloth in Cloth.objects.filter(brand=brand_name):
            itemsf_ += [cloth]
            if len(itemsf_) == 4:
                lst += [itemsf_]
                itemsf_ = []
                globlal_i += 1
        if itemsf_:
            lst += [itemsf_]
        #----------------------------------#
        context["allitems"] = lst
        return dict(list(context.items()))
    
