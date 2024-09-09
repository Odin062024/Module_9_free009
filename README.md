# Module_9_free009

# Library App

## Instalacja
1. Skopiuj repozytorium.
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Uruchom aplikację: `python app.py`

## Funkcjonalności
- Dodawanie albumów
- Edycja albumów
- Wyświetlanie listy albumów


Metody w API:
GET /api/library/ – Pobiera całą listę albumów.
GET /api/library/<int:item_id>/ – Pobiera szczegóły albumu o podanym id.
POST /api/library/ – Dodaje nowy album (przyjmuje dane w formacie JSON).
PUT /api/library/<int:item_id>/ – Aktualizuje istniejący album.
DELETE /api/library/<int:item_id>/ – Usuwa album o podanym id.


# Library API

## Instalacja
1. Skopiuj repozytorium.
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Uruchom aplikację: `python api.py`

## Endpointy
- `GET /api/library/` - Pobierz wszystkie albumy
- `GET /api/library/<id>/` - Pobierz szczegóły albumu o podanym ID
- `POST /api/library/` - Dodaj nowy album (wymaga danych JSON)
- `PUT /api/library/<id>/` - Zaktualizuj album o podanym ID (wymaga danych JSON)
- `DELETE /api/library/<id>/` - Usuń album o podanym ID

## Przykłady
### Dodanie albumu
```bash
curl -X POST http://127.0.0.1:5000/api/library/ -H "Content-Type: application/json" -d '{"title": "New Album", "artist": "Artist Name"}'
