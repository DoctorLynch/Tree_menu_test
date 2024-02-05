from django.urls import path
from menu.apps import MenuConfig
from menu.views import draw_menu

app_name = MenuConfig.name

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]
