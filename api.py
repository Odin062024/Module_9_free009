from flask import Flask, jsonify, request, abort
from models import library

app = Flask(__name__)

@app.route('/api/library/', methods=['GET'])
def get_library():
    """Zwraca całą listę albumów."""
    return jsonify(library.all()), 200

@app.route('/api/library/<int:item_id>/', methods=['GET'])
def get_album(item_id):
    """Zwraca szczegóły jednego albumu."""
    try:
        album = library.get(item_id - 1)
        return jsonify(album), 200
    except IndexError:
        abort(404, description="Album not found")

@app.route('/api/library/', methods=['POST'])
def add_album():
    """Dodaje nowy album do biblioteki."""
    if not request.json or 'title' not in request.json:
        abort(400, description="Bad request. Title is required.")
    
    new_album = {
        'title': request.json['title'],
        'artist': request.json.get('artist', ''),
        'description': request.json.get('description', ''),
        'is_listened': request.json.get('is_listened', False)
    }
    library.create(new_album)
    library.save_all()
    return jsonify(new_album), 201

@app.route('/api/library/<int:item_id>/', methods=['PUT'])
def update_album(item_id):
    """Aktualizuje informacje o istniejącym albumie."""
    try:
        album = library.get(item_id - 1)
    except IndexError:
        abort(404, description="Album not found")

    if not request.json:
        abort(400, description="Bad request. No data provided.")

    album['title'] = request.json.get('title', album['title'])
    album['artist'] = request.json.get('artist', album['artist'])
    album['description'] = request.json.get('description', album['description'])
    album['is_listened'] = request.json.get('is_listened', album['is_listened'])

    library.update(item_id - 1, album)
    library.save_all()
    return jsonify(album), 200

@app.route('/api/library/<int:item_id>/', methods=['DELETE'])
def delete_album(item_id):
    """Usuwa album z biblioteki."""
    try:
        album = library.get(item_id - 1)
    except IndexError:
        abort(404, description="Album not found")

    library.library.pop(item_id - 1)
    library.save_all()
    return jsonify({'result': True}), 204

if __name__ == "__main__":
    app.run(debug=True)
