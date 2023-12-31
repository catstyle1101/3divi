Тестовое задание для компании 3divi (1 Этап)

<details>

<summary>Содержание задания</summary>

Тестовое задание

Backend Developer Python

# User Story
Я, как пользователь системы контроля и управления доступом (СКУД), хочу
иметь возможность загружать в систему архивные видео для обработки. Хочу иметь
следующие возможности:

- Загружать несколько видео-файлов на обработку

- Получать список загруженных видео, их статус и прогресс обработки

- Остановить/отменить обработку конкретного видео

- Получать информацию о количестве людей на каждом видео

- Заносить в базу людей из видео

- Получать список людей с информацией на каком видео каждый был
обнаружен

- Вносить личные данные людей (ФИО, дату рождения, пол)

# Тестовая задача

Тестовое задание разделено на два этапа:

1. Разработка сервиса обработки загруженных видео

2. Разработка сервиса учета людей/сотрудников

Для сдачи тестового задание достаточно выполнить 1 этап

## 1 этап:

Реализовать сервис видеообработки на Django/FastApi/Flask, который бы
позволил детектировать лица на видео и возвращать пользователю агрегированные
данные: общее количество лиц по всем кадрам видео.

### Сервис должен предоставлять функции:

● Загрузка и обработка видео-файлов, выбранных пользователем.

● Получение списка загруженных видео (включая текущий статус, прогресс
выполнения и результат обработки).

● Остановка/отмена обработки выбранного видео.

## 2 этап
Используя сервис разработанный на первом этапе, расширить функционал
приложения. Сервис учета людей/сотрудников должен позволить пользователю
управлять базой профилей людей: вносить ФИО, пол, год рождения, а также получать
кроп изображения из видео, на основе которого был создан профиль. Заполнение базы
профилей должно происходить автоматически, включением настройки при загрузке
видео: На каждое найденное лицо в обрабатываемом видео, создается его профиль.

### Сервис должен предоставлять функции:

● Получение списка всех профилей (включая изображение из видео, ФИО, пол,
дату рождения и ссылку на обработанное видео)

● Внесение данных для каждого профиля (ФИО, пол, дата рождения)

● Удаление выбранного профиля

### Требования к реализации

● Программный интерфейс может быть произвольным, но должен быть описан в
формате OpenAPI/Swagger или GraphQL Schema;

Сервис должен предоставлять функции:

● Получение списка всех профилей (включая изображение из видео, ФИО, пол,
дату рождения и ссылку на обработанное видео)

● Внесение данных для каждого профиля (ФИО, пол, дата рождения)

● Удаление выбранного профиля
Требования к реализации

● Программный интерфейс может быть произвольным, но должен быть описан в
формате OpenAPI/Swagger или GraphQL Schema;

● Сервис видеобработки должен быть асинхронным и использовать ресурс
многоядерного процессора для кратного ускорения обработки, количество
одновременно обрабатываемых видеопотоков должно быть равно количеству
ядер;

● При запросе списка загруженных видео для каждого из них должны быть
доступны: текущий прогресс (значение от 0 до 100) и промежуточный результат
(количество найденных лиц на уже обработанном отрезке видео);

● Получение списка профилей не должно занимать более 1 секунды для 100
записей на одноядерном процессоре:

● Для метаданных профилей должна быть валидация данных (кол-во строк ФИО,
корректность введенной даты рождения, корректность введенного пола профиля)

Дополнительно

● Для детектирования лиц и получение кропов лиц можно использовать OpenCV.

Будет плюсом

● Микросервисная архитектура, с описанием процессов в виде UML диаграммы

● Контейнеризация docker для каждого сервиса, деплоймент при помощи
docker-compose

● Использование объектного хранилища с S3 интерфейсом, например MinIO

● Автотест в виде python скрипта

</details>

## Запуск проекта

```
git clone git@github.com:catstyle1101/3divi.git
cd 3divi
cp .env.example .env
docker compose up --build
# Может занять значительное время.
```

После запуска контейнеров проект доступен по адресу:

http://127.0.0.1:8000/

Также доступен Flower для просмотра задач celery

http://127.0.0.1:5555/tasks

Документация API:

http://127.0.0.1:8000/api/docs/

Реализована админка

http://127.0.0.1:8000/admin/

Для работы в админке понадобится создать учетную запись администратора

```
docker exec -it 3divi_backend_1 sh
python manage.py createsuperuser
# и следовать шагам мастера создания пользователя

```

## Возможности системы

- Пользователь может залить до 5 (размер и количество можно изменить в настройках) видео.
- Система автоматически ставит видео в очередь для распознавания лиц. Ведет подсчет и записывает данные в БД.
- Можно поставить распознавание на паузу, можно остановить распознавание (для нового запуска видео придется залить заново)
- Просмотреть текущий статус обработки видео можно на главной странице.
- Для теста добавлено видео в репозиторий, faces.mp4.

## Стек

- Django
- Celery
- Flower
- Face Recognition
- OpenCV2
- Redis
- Docker
- PostgreSQL
