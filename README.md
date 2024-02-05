Запуск проекта в dev-режиме
Инструкция ориентирована на операционную систему windows и утилиту git bash. Для прочих инструментов используйте аналоги команд для вашего окружения.

Клонируйте репозиторий и перейдите в него в командной строке:
git clone https://github.com/DoctorLynch/Tree_menu_test.git
Установите и активируйте виртуальное окружение:
python -m venv venv
source venv/Scripts/activate
Установите зависимости из файла requirements.txt:
pip install -r requirements.txt
В папке с файлом manage.py выполните миграции:
python manage.py migrate
Создайте суперюзера, зайдите в админку:
python manage.py createsuperuser
В папке с файлом manage.py запустите сервер, выполнив команду:
python manage.py runserver
Перейдите в админку и добавьте несколько пунктов и подпунктов ваших меню (главное меню должно совпадать с переданным url Н: tree_main)
Открываем главную страницу и видим результат проделанной работы
