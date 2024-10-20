from django.urls import path
from .views import * 
urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('Brands/', Brands.as_view(), name='Brands'),
    path('Feedback/', Feedback, name='Feedback'),
    path('Backstage/', Backstage, name='Backstage'),
    path('Brands/Conjunctiva/', Conjunctiva.as_view(), name='Conjunctiva'),
    path('Brands/hikikomori Kai/', HikikomoriKai.as_view(), name='hikikomoriKai'),
    path('Brands/Convulsive/', Convulsive.as_view(), name='Convulsive'),
    path('Brands/Iseedeadpeople/', Iseedeadpeople.as_view(), name='iseedeadpeople'),
    path('Brands/<str:brand_name>/<int:id>/', indexItem),
]