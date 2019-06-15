import re
import time
from time import mktime
from datetime import datetime
from django.http import HttpResponse
import requests
import lxml
from bs4 import BeautifulSoup
from .models import Editorial
from django.shortcuts import render, redirect
from time import mktime
import pytz

def home(request):
    return HttpResponse("¡Hola!")

def today_editorial(request):

    ec_editorial = requests.get("https://elcomercio.pe/opinion/editorial")

    ec_editorial_scr = ec_editorial.content

    soup = BeautifulSoup(ec_editorial_scr)

    enlace = soup.find('a', class_='page-link')

    titulo = soup.find('h2', class_='flow-title').find('a', class_='page-link').getText().strip()

    texto = soup.find('p', class_='flow-summary').getText().strip()

    tz = pytz.timezone('America/Bogota')
    
    fecha = soup.find('time')['datetime']
    fecha = time.localtime(int(fecha))
    fecha = datetime.fromtimestamp(mktime(fecha)).date()

    imagen = soup.find('source')["data-srcset"]

    full_url = "https://elcomercio.pe" + enlace['href']

    # today_date = datetime.now().date().strftime('%d %b %Y')
    today_date = datetime.now(tz).date()
    
    try:
        todays_editorial = Editorial.objects.get(date = datetime.now(tz).date())
        print("Se obtuvo la editorial de la BD")
    except:    
        todays_editorial = Editorial.objects.create(
            date = fecha,
            title = titulo,
            body = texto,
            url = full_url,
            image = imagen
        )

    editorials = Editorial.objects.all().order_by('-id') 
    
    return render(request, 'editorial/index.html', {'editorials': editorials, 'todays_editorial': todays_editorial, 'full_url': full_url})