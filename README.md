# Wildberries Analytics

**Wildberries Analytics** — сервис для сбора, хранения и визуализации аналитики по товарам с платформы Wildberries.

## Возможности

- Парсинг товаров с Wildberries по категории
- Сохранение информации о товарах в базу данных Django
- REST API с фильтрацией по цене, рейтингу и количеству отзывов
- Веб-интерфейс с таблицей товаров и графиками (распределение цен, скидки vs рейтинг)

---

## Установка и запуск

### 1. Клонирование и подготовка окружения

```bash
git clone https://github.com/your-username/wildberries_analytics.git
cd wildberries_analytics

python -m venv .venv
source .venv/bin/activate  # для macOS/Linux
# .venv\Scripts\activate   # для Windows

pip install -r requirements.txt
```

### 2. Миграции базы данных

```bash
python manage.py migrate
```

### 3. Парсинг товаров

Для наполнения базы товаров используйте парсер по категории (пример для ноутбуков):

```bash
python manage.py shell
```
```python
from analytics.parser import parse_products_by_category
parse_products_by_category()
exit()
```

### 4. Запуск сервера

```bash
python manage.py runserver
```

Откройте [http://127.0.0.1:8000/](http://127.0.0.1:8000/) в браузере.

---

## Структура проекта

```
wildberries_analytics/
├── manage.py
├── requirements.txt
├── analytics/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── parser.py
│   ├── templates/
│   │   └── analytics/
│   │       └── dashboard.html
│   ├── static/
│   │   └── analytics/
│   │       └── charts.js
│   └── management/
│       └── commands/
│           └── parse_wb.py
├── wildberries_analytics/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
```

---

## Примечания

- Для корректной работы парсера используйте актуальные категории Wildberries.
- Если API Wildberries изменится, потребуется обновить парсер.

