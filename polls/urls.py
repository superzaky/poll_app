from django.conf.urls import url

from . import views

#Our URLconf to map a view to a URL so that we can call a view. 
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
