from django.shortcuts import render
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.



def home2(request):
    return render(request, 'index2.html')



def home3(request):
    url = f"https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr{ api_key}"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)