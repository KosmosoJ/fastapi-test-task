# fastapi Test Task

## Библиотеки

Для приложения используются библиотеки FastAPI и Sqlalchemy на движке Asyncpg

## Установки

### Запуск вне Docker

Необходимо создать файл __.env__ на подобии с __.env.template__

Создать виртуальное окружение __python -m venv .venv__ и установить зависимости __pip install app/requirements.txt__

Для запуска приложения использовать в терминале __uvicorn main:app__

### Запуск в Docker 

Использовать команду __docker-compose up__

Используется стандартный порт - __8000__

## Использование

- __/products__ (get) вывод всех продуктов из бд

- __/products__ (post) создание продукта

- __/products/{product_id}__ (get) просмотр продукта по ID

- __/products/{product_id}__ (put) изменение продукта по ID

- __/products/{product_id}__ (delete) удаление продукта по ID

- __/orders__ (get) получение всех заказов из бд

- __/orders__ (post) создание заказа {"product_id": 0,"quantity": 0}

- __/orders/{order_id}__ (get) получение информации о заказе, для поиска используется order.order_id

- __/orders/{order_id}/status__ (patch) изменение статуса заказа. Изменяется статус только в одну сторону - в процессе -> отправлен -> доставлен. Для ID используется order.order_id

## Информация

Swagger стандартный от FastAPI - [/docs](http://localhost:8000/docs)