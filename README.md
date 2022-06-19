# Тестовое задание

Функциональные требования:

У системы должны быть методы API, которые обеспечивают
1. Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
2. Добавление комментария к статье.
3. Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
4. Получение всех комментариев к статье вплоть до 3 уровня вложенности.
5. Получение всех вложенных комментариев для комментария 3 уровня.
6. По ответу API комментариев можно воссоздать древовидную структуру.
7. Возможность поставить лайк статье
8. Возможность поставить дизлайк статье
9. Авторизация через токен
10. Регистрация, аутентификация

Нефункциональные требования:
1. Использование Django ORM.
2. Следование принципам REST.
3. Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
4. Решение в виде репозитория на Github, Gitlab или Bitbucket.
5. readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt.
6. Использование свежих версий python и Django.

На реализацию тестового задания отводится 2 дня с момента прочтения сообщения.


## Установка

1. Скачать проект
   - git clone https://github.com/Zaraza88/blog_api.git
2. Добавить виртуальное окружение
   - python3 -m venv venv  (или python -m venv venv)
3. Активировать виртуальное окружение
```
   Linux - source venv/bin/activate
   Windows - venv\Scripts\activate.bat
```
4. Установите зависимости в виртуальное окружение.

```
   - pip install -r requirements. txt
```
## Запуск проекта
#### Если вы используете Linux, то следует писать **./manage.py**, если Windows - **python manage.py**
1. Создать миграции
```
   ./manage.py makemigrations
   ./manage.py migrate
```
2. Создать суперюзера
```
   ./manage.py createsuperuser
```
3. Запустить сервер
```
   ./manage.py runserver
```
### Для навигации использовать либо автодокументацию - **http://127.0.0.1:8000/swagger/**, либо:
```
http://127.0.0.1:8000/api/v1/post/ - Вывод всписка всех постов
http://127.0.0.1:8000/api/v1/create_post/ - Создать пост
http://127.0.0.1:8000/api/v1/post/1/ - Вывод первого поста по его id
http://127.0.0.1:8000/api/v1/comment/ - Создать комментарий
http://127.0.0.1:8000/api/v1/post_deteil_comment/1/ - Вывод всех комментарие первого поста
http://127.0.0.1:8000/api/v1/self_comment/1/ - Вывод вложенных комментариев первого поста
http://127.0.0.1:8000/api/v1/like/ - Поставить лайк/дизлайк посту
```




