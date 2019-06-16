import re
import time
from time import mktime
from datetime import datetime, timedelta
from django.http import HttpResponse
import requests
import lxml
from bs4 import BeautifulSoup
from .models import Editorial
from django.shortcuts import render, redirect
from time import mktime
import pytz


def today_editorial(request):

    editorials = Editorial.objects.all().order_by('-id') 
    
    tz = pytz.timezone('America/Bogota')
    today_date = datetime.now(tz).date()
    yesterday_date = today_date - timedelta(days=1)
    
    try:
        today_editorial = Editorial.objects.get(date = today_date)
        if today_editorial:
            return render(request, 'editorial/index.html', {'editorials': editorials, 'today_editorial': today_editorial})
    except:
        yesterday_editorial = Editorial.objects.get(date = yesterday_date)
        if yesterday_editorial:
            return render(request, 'editorial/index.html', {'editorials': editorials, 'yesterday_editorial': yesterday_editorial})    

   
        
    