# Mojarung site

## Как запустить

1. Версия Python должна быть не ниже 3.12.3
2. Создать виртуальное окружение и активировать его
3. Выполнить команду `pip install -r requirements.txt`
4. В корне проекта создать файл `.env` и заполнить его в соответствии с файлом `.env.example`, заменяя заглушки секретными
   ключами
5. Выполнить команду `python manage.py runserver`

## Во время разработки

1. Не трогать содержимое папки `static` в корне проекта - эта папка пересоздаётся автоматически
2. Чтобы открыть улучшенную оболочку (позволяет видеть sql запросы для ORM команд), нужно выполнить команду `python manage.py shell_plus --print-sql`

## Перед деплоем

1. Выполнить команду `python manage.py collectstatic`
2. Выполнить команду `python manage.py runserver`
3. В `settings.py` установить `DEBUG = False` и заполнить `ALLOWED_HOSTS`
