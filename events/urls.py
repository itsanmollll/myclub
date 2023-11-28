from django.urls import path

from . import views

urlpatterns = [
    # Path Converters:
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphe-and_underscores_stuff
    # UUID: Universally unique identifier
    #path('',views.home, name="home"),
    path('<int:year>/<str:month>/',views.home, name="home"),
]