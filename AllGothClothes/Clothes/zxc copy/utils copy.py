from .models import *
from typing import Any
from django.views.generic import ListView
menu = [{'title': 'BRANDS', 'url_name': 'Brands'},
        {'title': 'FEEDBACK', 'url_name': 'Feedback'},
        {'title': 'BACKSTAGE', 'url_name': 'Backstage'},
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
        title = str(context["view"]).split()[0][15:]
        #---Распределение вещей по рядам---#
        itemsf_ = []
        allitems = {}
        globlal_i= 1
        allitems["title"] = title
        allitems["menu"] = menu
        for i in context["posts"]:
            itemsf_ += [i]
            if len(itemsf_) == 4:
                allitems[f"items{globlal_i}"] = itemsf_
                itemsf_ = []
                globlal_i += 1    
        if itemsf_:
            allitems[f"items{globlal_i}"] = itemsf_
        #----------------------------------#
        return dict(list(context.items()) + list(allitems.items()))
    
