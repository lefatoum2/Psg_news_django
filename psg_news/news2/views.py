from django.shortcuts import render
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
api_key = os.getenv("api_key")
api_key2 = os.getenv("api_key2")



def temp1():
    city = 'Paris, PA'
    url = f'https://api.weatherbit.io/v2.0/current?&city={city}&key={api_key2}&include=minutely'
    response = requests.get(url)
    data = response.json()['data'][0]
    return data




def home4(request):
    url = f"https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr{ api_key}"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    date1 = datetime.now()
    weather = temp1()
    context={
    'data':content_from_internet,'date1':date1, 'weather1':weather
    }
    return render(request,'index5.html',context)


