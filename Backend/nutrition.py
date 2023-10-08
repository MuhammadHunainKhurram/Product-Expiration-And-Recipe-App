# Takes 'barcode' barcode value and makes API call to Open Food Facts API

import requests

def fetch_nutrition(barcode):
    # API URL
    base_url = 'https://world.openfoodfacts.org/api/v0/product/'
    url = f'{base_url}{barcode}.json'

    try:
        # PAI request
        response = requests.get(url)

        if response.status_code == 200:
            # parse JSON
            data = response.json()
            if 'product' in data:
                # Extract relevant details such as product name, ingredients, etc.
                info = data['product']
                name = (info.get('brands', 'n/a') + " " + info.get('product_name', 'n/a')).strip().replace(",","")
                ingredients = [ingredient.replace('en:', '').strip() for ingredient in info.get('ingredients_analysis_tags', [])]
                allergens = info.get('allergens', 'n/a').replace('en:', '').strip()
                serving = info.get('serving_size', 'n/a')
                score = info.get('nutrition_grades', 'n/a').capitalize()
                nutrition = info.get('nutriments', {})
                energy = nutrition.get('energy-kcal_serving', 'n/a')
                protein = nutrition.get('proteins_serving', 'n/a')
                fat = nutrition.get('fat_serving', 'n/a')
                carbs = nutrition.get('carbohydrates_serving', 'n/a')
                sodium = nutrition.get('sodium_serving', 'n/a')
                sugar = nutrition.get('sugars_serving', 'n/a')
                fiber = nutrition.get('fiber_serving', 'n/a')
                chol = nutrition.get('cholesterol_serving', 'n/a')
                return {
                    'Name': name,
                    'Nutrition Score': score,
                    'Ingredient Analysis': ingredients,
                    'Allergens': allergens,
                    'Serving Size': serving,
                    'Calories per Serving': energy,
                    'Protein (g)': protein,
                    'Fat (g)': fat,
                    'Carbs (g)': carbs,
                    'Sodium (g)': sodium,
                    'Sugar (g)': sugar,
                    'Fiber (g)': fiber,
                    'Cholesterol (g)': chol
                }
            else:
                return None
        else:
            return None
    except Exception as e:
        return None

def main():
    barcode = '3045140105502'

    # Fetch product information
    result = fetch_nutrition(barcode)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Name: {result['Name']}")
        print(f"Nutrition Score: {result['Nutrition Score']}")
        print(f"Ingredient Analysis: {result['Ingredient Analysis']}")
        print(f"Allergens: {result['Allergens']}")
        print(f"Serving Size: {result['Serving Size']}")
        print(f"Calories per serving: {result['Calories per Serving']}")
        print(f"Protein (g): {result['Protein (g)']}")
        print(f"Fat (g): {result['Fat (g)']}")
        print(f"Carbs (g): {result['Carbs (g)']}")
        print(f"Sodium (g): {result['Sodium (g)']}")
        print(f"Sugar (g): {result['Sugar (g)']}")
        print(f"Fiber (g): {result['Fiber (g)']}")
        print(f"Cholesterol (g): {result['Cholesterol (g)']}")

if __name__ == "__main__":
    main()

