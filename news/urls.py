from django.conf.urls import url
from . import views

#naming a url helps us to refer to it from elsewhere in project

urlpatterns =[
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^today/$', views.news_of_day, name = 'newsToday')
]