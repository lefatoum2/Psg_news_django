from django.shortcuts import render
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
api_key = os.getenv("api_key")


def home2(request):
    return render(request, 'index2.html')



def home3(request):
    url = f"https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr{ api_key}"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    date1 = datetime.now()
    context={
    'data':content_from_internet,'date1':date1
    }
    return render(request,'index3.html',context)


def home4(request):
    url = f"https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr{ api_key}"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    date1 = datetime.now()
    context={
    'data':content_from_internet,'date1':date1
    }
    return render(request, 'index5.html', context)