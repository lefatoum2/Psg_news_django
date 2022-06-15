from django.urls import path 
from .views import home_view, usa_view, france_view, world_view, necro_view


urlpatterns = [
path('',home_view,name='home'),
path('usa',usa_view,name='usa'),
path('france',france_view,name='france'),
path('world',world_view,name='world'),
path('necro',necro_view,name='necro'),
]