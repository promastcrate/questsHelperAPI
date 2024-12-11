# questsHelperAPI

Скачиваем зависимости -> pip install -r requirements.txt

После этого создаем миграции и выполянем их 
python manage.py makemigrations core 
python manage.py migrate

Далее наполняем БД при помощи скрипта populateDB
Далее запускаем проект -> python manage.py runserver 

