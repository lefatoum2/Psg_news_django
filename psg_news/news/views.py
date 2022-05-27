from django.shortcuts import render
import requests
import json
# Create your views here.


def home_view(request):
    url = "https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def usa_view(request):
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)




def world_view(request):
    url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def france_view(request):
    url = "https://newsapi.org/v2/top-headlines?country=fr&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def necro_view(request):
    url = "https://newsapi.org/v2/top-headlines?q=died&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)