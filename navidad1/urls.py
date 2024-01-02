"""
URL configuration for navidad1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Aplicaciones.Navidad1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Navidad1.urls')),
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

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
