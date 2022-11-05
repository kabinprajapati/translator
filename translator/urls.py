from xml.dom import DomstringSizeErr
from . import views
from django.urls import path

urlpatterns = [
    path('', views.translator_view, name='translator_view')
]
