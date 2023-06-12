from django.urls import path
from .views import index, contato, w3c


urlpatterns = [path("",index,name='index'), path("contato",contato, name='contato'), 
               path("w3c",w3c, name='w3c'),]



