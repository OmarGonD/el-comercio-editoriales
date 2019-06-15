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


def today_editorial(request):

    tz = pytz.timezone('America/Bogota')
    
    today_date = datetime.now(tz).date()

    todays_editorial = Editorial.objects.get(date = today_date)
     
    editorials = Editorial.objects.all().order_by('-id') 
    
    return render(request, 'editorial/index.html', {'editorials': editorials, 'todays_editorial': todays_editorial})