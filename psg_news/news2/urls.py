from django.urls import path , include
from .views import home2, home3, home4


urlpatterns = [
path('',home4,name='home4'),
]