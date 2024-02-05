from django.urls import path
from menu.apps import MenuConfig
from menu.views import my_view

app_name = MenuConfig.name

urlpatterns = [
    path('', my_view, name='menu')
]
