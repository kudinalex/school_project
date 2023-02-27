from django.urls import path
from . import views
urlpatterns = [
    path('',views.infotex_home,name='infotex_home')
    ]