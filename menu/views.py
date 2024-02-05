from django.shortcuts import render
from menu.models import MenuItem


def my_view(request):
    # Получите название меню из параметров запроса или из другого источника
    menu_name = request.GET.get('menu_name', 'main_menu')
    menu_items = MenuItem.objects.filter(name=menu_name)

    return render(request, 'menu/menu.html', {'menu_items': menu_items, 'request': request})
