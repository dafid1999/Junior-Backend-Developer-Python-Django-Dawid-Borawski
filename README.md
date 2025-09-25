# Django Project

Startowy projekt Django.

## Wymagania

- Python 3.8+
- Django 5.0+

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Utwórz środowisko wirtualne:
```bash
python -m venv venv
```

3. Aktywuj środowisko wirtualne:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

5. Uruchom migracje:
```bash
python manage.py migrate
```

6. Utwórz superusera (opcjonalne):
```bash
python manage.py createsuperuser
```

7. Uruchom serwer deweloperski:
```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/

## Struktura projektu

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Przydatne komendy

- `python manage.py runserver` - uruchom serwer deweloperski
- `python manage.py migrate` - wykonaj migracje bazy danych
- `python manage.py makemigrations` - utwórz nowe migracje
- `python manage.py createsuperuser` - utwórz superusera
- `python manage.py collectstatic` - zbierz pliki statyczne
- `python manage.py test` - uruchom testy
