from django.conf.urls import url
from . import views

#naming a url helps us to refer to it from elsewhere in project

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]