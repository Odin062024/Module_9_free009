from flask import Flask, request, render_template, redirect, url_for
from forms import LibraryForm
from models import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "sekretny_klucz"

@app.route("/library/", methods=["GET", "POST"])
def library_list():
    form = LibraryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            library.create(form.data)
            library.save_all()
        return redirect(url_for("library_list"))

    return render_template("library.html", form=form, library=library.all(), error=error)

@app.route("/library/<int:item_id>/", methods=["GET", "POST"])
def library_details(item_id):
    item = library.get(item_id - 1)
    form = LibraryForm(data=item)

    if request.method == "POST":
        if form.validate_on_submit():
            library.update(item_id - 1, form.data)
        return redirect(url_for("library_list"))
    return render_template("library_item.html", form=form, item_id=item_id)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/api/library/sort/<string:by>/', methods=['GET'])
def sort_library(by):
    """Sortowanie albumów po tytule lub artyście."""
    if by == 'title':
        sorted_library = sorted(library.all(), key=lambda x: x['title'])
    elif by == 'artist':
        sorted_library = sorted(library.all(), key=lambda x: x['artist'])
    else:
        abort(400, description="Invalid sorting parameter")
    return jsonify(sorted_library), 200
