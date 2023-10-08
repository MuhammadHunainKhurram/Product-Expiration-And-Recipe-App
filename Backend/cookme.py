from barcode_reader import read_barcode
from nutrition import fetch_nutrition
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save_ingredient():
    if request.method == 'POST':
        ingredient = request.form['ingredient']

        # Handle photo upload
        photo = request.files.get('photo')
        if photo:
            # You can save the photo to a folder, perform processing, or display it as needed
            # Here, we'll just print the filename
            photo_filename = photo.filename
            print(f"Received photo: {photo_filename}")

    return redirect(url_for('index'))


@app.route('/barcode', methods=['PUT'])
def get_food():
    if request.method == 'PUT':
        barcode = read_barcode(request.json['image'])
        return fetch_nutrition(barcode)


if __name__ == "__main__":
    app.run(debug=True)
