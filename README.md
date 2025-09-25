# Django Project

Startowy projekt Django.

## Wymagania

- Python 3.10+
- Django 5.x

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

5. Zmienne środowiskowe:
```bash
cp .env.example .env
# uzupełnij SECRET_KEY, opcjonalnie zmień MAX_UPLOAD_SIZE_MB
```

6. Migracje bazy:
```bash
python manage.py migrate
```

7. Uruchom serwer deweloperski:
```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/

## Struktura projektu

```
Python Django Developer/
├─ manage.py
├─ pytest.ini
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ README.md
├─ static/
│  └─ css/
│     └─ style.css
├─ templates/
│  ├─ base.html
│  └─ home.html
├─ myproject/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
├─ text_processor/
│  ├─ __init__.py
│  ├─ forms.py
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/text_processor/
│     ├─ upload.html
│     └─ result.html
├─ pesel_validator/
│  ├─ __init__.py
│  ├─ forms.py
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/pesel_validator/
│     └─ validate.html
└─ tests/
   ├─ test_pesel.py
   ├─ test_text_processor.py
   └─ test_upload_form.py
```

## Konfiguracja

- SECRET_KEY: tajny klucz Django (w .env)
- DEBUG: 0/1 (w .env)
- ALLOWED_HOSTS: lista hostów (w .env)
- MAX_UPLOAD_SIZE_MB: maksymalny rozmiar uploadu pliku .txt (domyślnie 5 MB)

## Uruchamianie testów

```
pytest -q
```

Zakres testów:
- Walidator PESEL (poprawność, suma kontrolna, data, płeć, heurystyka powtarzalnych cyfr)
- Przetwarzanie tekstu (mieszanie, interpunkcja, krótkie słowa)
- Walidacja formularza uploadu (limit rozmiaru pliku)

## Opis zadań

- Zadanie 1: Aplikacja do przetwarzania tekstu – upload .txt, mieszanie liter wewnątrz wyrazów, wynik na stronie.
- Zadanie 2: Walidator PESEL – formularz, weryfikacja wg specyfikacji, data urodzenia i płeć, heurystyka sztucznych numerów.
