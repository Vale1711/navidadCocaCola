from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', {'navbar': 'index'})

def marcas(request):
    return render(request, 'marcas.html', {'navbar': 'marcas'})

def navidad(request):
    return render(request, 'navidad.html', {'navbar': 'navidad'})

def power(request):
    return render(request, 'power.html', {'navbar': 'power'})

def sprite(request):
    return render(request, 'sprite.html', {'navbar': 'sprite'})

def historia(request):
    return render(request, 'historia.html', {'navbar': 'historia'})

def terminos(request):
    return render(request, 'terminos.html', {'navbar': 'terminos'})

def trabaja(request):
    return render(request, 'trabaja.html', {'navbar': 'trabaja'})

def mapa(request):
    return render(request, 'mapa.html', {'navbar': 'mapa'})

def contactos(request):
    return render(request, 'contactos.html', {'navbar': 'contactos'})

def fanta(request):
    return render(request, 'fanta.html', {'navbar': 'fanta'})

def sustentabilidad(request):
    return render(request, 'sustentabilidad.html', {'navbar': 'sustentabilidad'})

def social(request):
    return render(request, 'social.html', {'navbar': 'social'})

def prensa(request):
    return render(request, 'prensa.html', {'navbar': 'prensa'})

def politica(request):
    return render(request, 'politica.html', {'navbar': 'politica'})
