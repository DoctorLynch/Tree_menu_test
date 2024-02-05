                                                             Запуск проекта в dev-режиме
Инструкция ориентирована на операционную систему windows и утилиту git bash. Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:
git clone https://github.com/DoctorLynch/Tree_menu_test.git
2. Установите и активируйте виртуальное окружение:
python -m venv venv
source venv/Scripts/activate
3. Установите зависимости из файла requirements.txt:
pip install -r requirements.txt
4. В папке с файлом manage.py выполните миграции:
python manage.py migrate
5. Создайте суперюзера, зайдите в админку:
python manage.py createsuperuser
6. В папке с файлом manage.py запустите сервер, выполнив команду:
python manage.py runserver
7. Перейдите в админку и добавьте несколько пунктов и подпунктов ваших меню (главное меню должно совпадать с переданным url Н: tree_main)
8. Открываем главную страницу и видим результат проделанной работы
