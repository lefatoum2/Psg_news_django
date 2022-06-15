from django.urls import path , include
from .views import home2, home3, home4


urlpatterns = [
path('home2',home2,name='home2'),
path('home3',home3,name='home3'),
path('',home4,name='home4'),
]