from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns=[
    path('home/',views.home,name='news-home'),
    path('sports/',views.sports,name='news-sports'),
    path('health/',views.health,name='news-health'),
    path('science/',views.science,name='news-science'),
    path('technology/',views.technology,name='news-tech'),
    path('business/',views.business,name='news-business'),
    #path('<str:value1>/',views.summarize,name='news-summ')
    path('<str:value1>/',views.summarize,name='news-summ')
    #path('<str:value1><str:value2>/',views.summarize,name='news-summ')
    #url(r'^(?P<value1>\w+)/$', views.summarize, name='news-summ')
    #url(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', views.summarize, name='news-summ')
    #url(r'^(?P<value1>\w+?)(?P<value2>\w+?)$', views.summarize, name='news-summ')
    #url(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[/]', views.summarize, name='news-summ')
    
]