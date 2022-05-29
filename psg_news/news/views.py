from django.shortcuts import render
import requests
import json
import config

# Create your views here.


def home_view(request):
    url = "https://newsapi.org/v2/top-headlines?q=psg&category=sport&country=fr" + api_key
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def usa_view(request):
    url = "https://newsapi.org/v2/top-headlines?country=us"+ api_key
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)




def world_view(request):
    url = "https://newsapi.org/v2/top-headlines?language=en"+ api_key
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def france_view(request):
    url = "https://newsapi.org/v2/top-headlines?country=fr"+ api_key
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)


def necro_view(request):
    url = "https://newsapi.org/v2/top-headlines?q=died" + api_key
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)