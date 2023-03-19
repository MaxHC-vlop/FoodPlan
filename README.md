# Сайт с рецептами сервиса FoodPlan

Это сайт для оформления подписки на сервис с планами питания, которые будут формировать нужный индивидуальный план с рецептами на каждый день .

- На сайте есть два независимых интерфейса.

- `Первый` интерфейс предназначен для пользователя. Здесь он может увидеть примеры предложенных рецептов. Пройти регистрацию и авторизацию. Так же оформить подписку.

- `Второй` интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта.

### Запуск приложения

Скачайте код:
```sh
git clone git@github.com:MaxHC-vlop/FoodPlan.git
```

Перейдите в каталог проекта:
```sh
cd FoodPlan
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.9.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3.9`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии. 

В каталоге проекта создайте виртуальное окружение:
```sh
python3 -m venv venv
```

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменные окружения . Создать файл `.env` в каталоге `FoodPlan/` и положите туда такой код:
```sh
SECRET_KEY='SECRET_KEY'
DEBUG=('DEBUG', True)
CSRF_TRUSTED_ORIGINS=('CSRF_TRUSTED_ORIGINS'
ALLOWED_HOSTS=('ALLOWED_HOSTS', ['127.0.0.1', 'localhost'])
EMAIL_HOST=('EMAIL_HOST', default='smtp.yandex.ru')
EMAIL_PORT=('EMAIL_PORT', default=465)
EMAIL_HOST_USER=('EMAIL_HOST_USER', default='user')
EMAIL_HOST_PASSWORD=('EMAIL_HOST_PASSWORD', default='password')
EMAIL_USE_TLS=('EMAIL_USE_TLS', default=False)
EMAIL_USE_SSL=('EMAIL_USE_SSL', default=True)
```

Создайте файл базы данных SQLite и отмигрируйте её следующей командой:

```sh
python3 manage.py migrate
```

Запустите сервер:

```sh
python3 manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Если вы увидели пустую белую страницу, то не пугайтесь, выдохните. Просто фронтенд пока ещё не собран. Переходите к следующему разделу README.

### Собрать фронтенд


Теперь если зайти на страницу  [http://127.0.0.1:8000/](http://127.0.0.1:8000/), то вместо пустой страницы вы увидите:

## Как запустить prod-версию сайта

Настроить бэкенд: создать файл `.env` в каталоге `star_burger/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `CSRF_TRUSTED_ORIGINS` —
- `ALLOWED_HOSTS` —
- `EMAIL_HOST` —
- `EMAIL_PORT` —
- `EMAIL_HOST_USER` —
- `EMAIL_HOST_PASSWORD` —
- `EMAIL_USE_TLS` —
- `EMAIL_USE_SSL` —
