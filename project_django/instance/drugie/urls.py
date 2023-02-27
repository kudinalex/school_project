from django.urls import path
from . import views
urlpatterns = [
    path('',views.drugie_home,name='drugie_home'),]