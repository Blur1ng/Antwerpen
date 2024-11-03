from django.urls import include, path
from .views import *
urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('', Mainpage.as_view(), name='ANTWERPEN'),
    path('Brands/', Brands.as_view(), name='Brands'),
    path('Feedback/', Feedback.as_view(), name='Feedback'),
    path('News/', News.as_view(), name='News'),
    path('login/',include('login_user.urls')),
    path('Brands/Conjunctiva/', Conjunctiva.as_view(), name='Conjunctiva'),
    path('Brands/hikikomori Kai/', HikikomoriKai.as_view(), name='hikikomoriKai'),
    path('Brands/Convulsive/', Convulsive.as_view(), name='Convulsive'),
    path('Brands/iseedeadpeople/', Iseedeadpeople.as_view(), name='Iseedeadpeople'),
    path('Brands/<str:brand_name>/<str:cloth_name>', Cloth_detail.as_view(), name='cloth detail'),
    path('rate/', rate_cloth, name='rate_cloth'),
    path('srofl/', srofl, name="srofl"),
]