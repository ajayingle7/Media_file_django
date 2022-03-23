from django.urls import path
from .views import naukariView, getImage




urlpatterns  =[

    path("emp/", naukariView, name="naukari"),
    path("show/", getImage, name="image" )



]