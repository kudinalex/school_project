from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('main/img/favicon.ico'))),
]
