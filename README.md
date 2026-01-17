# FastAPI Notes API

Простое учебное REST API для заметок, написанное на FastAPI.  

## Стек

- Python 3.10+
- FastAPI
- Pydantic
- SQLite
- SQLAlchemy
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

| Method | Endpoint        | Description      |
|--------|-----------------|------------------|
| `POST` | `/api/notes/`   | Создать заметку |
| `GET`  | `/api/notes/`   | Все заметки     |
| `GET`  | `/api/notes/1`  | Одна заметка    |
| `PATCH`| `/api/notes/1`  | Обновить        |
| `DELETE`| `/api/notes/1`| Удалить        |

