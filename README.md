# Wildberries Analytics

Данный проект представляет собой простой сервис аналитики товаров с сайта Wildberries. Он включает в себя backend на Django с REST API и frontend с визуализацией данных.

## Возможности

- Парсинг данных с Wildberries по поисковому запросу.
- Сохранение информации о товарах в базе данных.
- API-эндпоинт `/api/products/` с фильтрацией по цене, рейтингу и количеству отзывов.
- Веб-интерфейс с таблицей товаров и графиками:
  - Гистограмма цен
  - Линейный график зависимости скидки от рейтинга
- Интерфейс с динамическими фильтрами и сортировкой данных.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone <your-repo-url>
   cd wildberries_analytics
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции:
   ```bash
   python manage.py migrate
   ```

5. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

6. Для запуска парсера выполните:
   ```bash
   python manage.py parse_wb "ваш_поисковый_запрос"
   ```

7. Перейдите в браузере:
   ```
   http://127.0.0.1:8000/
   ```

## Стек технологий

- Python, Django, Django REST Framework
- JavaScript, Chart.js
- SQLite (по умолчанию, можно заменить на PostgreSQL)