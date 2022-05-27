
## Installation

## Utilisation de NewsApi
Inscription sur https://newsapi.org/ et obtenez votre APi Key.


3 principales URLs :

- /v2/top-headlines
- /v2/everything
- /v2/sources


#### Exemple

newstrump = ('http://newsapi.org/v2/top-headlines?    

                       q=trump& # Mot clé recherché

                       country=us& # Choix du pays

                 category=general& # catégorie

                      language=en& # langue

                pageSize=30& # Nombre max de pages

                     apiKey=Your_api_key') # API Key



##### Pour aller plus loin 

On peut mettre ses données ou articles sous forme de Dataframe pour la création d'un modèle de classification des news(négative ou positive).

```
newstrumpheadlinesurlresponse = requests.get(newstrump)
```

```
newstrumpheadlines=newstrumpheadlinesurlresponse.json()
```

```
df =  pd.DataFrame(newstrumpheadlines)
```

## Views 
```py
def home_view(request):
    url = "https://newsapi.org/v2/top-headlines?country=fr&apiKey=35b15b6df19743a6b66dbfbb719bcea0"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    return render(request,'index.html',context)



```

## URLS

news/urls.py :
```py
from django.urls import path , include
from .views import home_view, usa_view, france_view, world_view, necro_view


urlpatterns = [
path('',home_view,name='home'),
path('usa',usa_view,name='usa'),
path('france',france_view,name='france'),
path('world',world_view,name='world'),
path('necro',necro_view,name='necro'),
]
```

psn_news/urls.py :
```py
from django.contrib import admin
from django.urls import path , include



urlpatterns = [
path('admin/', admin.site.urls),
path('',include('news.urls'))
]
```

## Template
index.html:
```html
{% extends 'main.html'%}

{% block content %}

{% for onedata in data.articles %}
<div class="col-sm">
<div class="card " style="width: 18rem;">
<img src="{{onedata.urlToImage}}" class="card-img-top" alt="{{onedata.source.name}}">
<div class="card-body ">
<h5 class="card-title ">{{onedata.title}}</h5>
<p class="card-text">{{onedata.description|truncatechars:150}}</p>
<a href="{{onedata.url}}" target="blank" class="btn btn-primary">Read</a>
    </div>
        </div>
            </div>
{% endfor %}

{% endblock content  %}

```

## Fin 

![img6](./img/2022-05-27a.jpg)