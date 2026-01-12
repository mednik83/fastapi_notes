# FastAPI Notes API

Простое учебное REST API для заметок, написанное на FastAPI.  
Данные хранятся в JSON-файле.

## Стек

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

## Установка и запуск (Linux)

### 1. Клонирование репозитория

```bash
git clone https://github.com/mednik83/fastapi_notes.git
cd fastapi_notes
```

### 2. Создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
uvicorn src.main:app --reload
```

После запуска API будет доступно по адресу:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

## Эндпоинты

- `GET /notes`
- `GET /notes/{id}`
- `POST /notes`
- `PUT /notes/{id}`
- `PATCH /notes/{id}`
- `DELETE /notes/{id}`
