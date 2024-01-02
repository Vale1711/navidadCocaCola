from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('marcas/', views.marcas, name='marcas'),
    path('navidad/', views.navidad, name='navidad'),
    path('power/', views.power, name='power'),
    path('sprite/', views.sprite, name='sprite'),
    path('historia/', views.historia, name='historia'),
    path('terminos/', views.terminos, name='terminos'),
    path('trabaja/', views.trabaja, name='trabaja'),
    path('mapa/', views.mapa, name='mapa'),
    path('contactos/', views.contactos, name='contactos'),
    path('fanta/', views.fanta, name='fanta'),
    path('sustentabilidad/', views.sustentabilidad, name='sustentabilidad'),
    path('social/', views.social, name='social'),
    path('prensa/', views.prensa, name='prensa'),
    path('politica/', views.politica, name='politica'),


]
