from barcode_reader import read_barcode
from nutrition import fetch_nutrition
from recipe import maker
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
import json

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

# takes an image, stores product info, returns info
@app.route('/barcode', methods=['PUT'])
def get_food():
    if request.method == 'PUT':
        barcode = read_barcode(request.json['image'])
        nutrition = fetch_nutrition(barcode)

        # store info on db
        if nutrition is not None:
            with open('Backend/db/data.json', 'r') as db:
                data = json.load(db)
        data["data"].append({"product": nutrition, "barcode": barcode})
        with open('Backend/db/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return nutrition
    
# takes list of items and returns recipes
@app.route('/recipe', methods=['PUT'])
def get_recipe():
    if request.method == 'PUT':
    
        with open('Backend/db/data.json', 'r') as db:
            data = json.load(db)

        product_names = [entry['product']['Name'] for entry in data['data']]
        recipe = maker(product_names)
        
        return recipe


if __name__ == "__main__":
    app.run(debug=True)
