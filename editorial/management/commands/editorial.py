from django.core.management.base import BaseCommand, CommandError
from editorial.models import Editorial
import re
import time
from time import mktime
from datetime import datetime
from django.http import HttpResponse
import requests
import lxml
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from time import mktime
import pytz

class Command(BaseCommand):

    def handle(self, **options):

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
            today_editorial = Editorial.objects.get(date = datetime.now(tz).date())
        except:    
            today_editorial = Editorial.objects.create(
                date = fecha,
                title = titulo,
                body = texto,
                url = full_url,
                image = imagen
            )
        

    