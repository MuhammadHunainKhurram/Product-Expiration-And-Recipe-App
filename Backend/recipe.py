import openai

def maker(listr):
  openai.api_key = ("")
  # listr = input("Provide the ingredients that you have: ")
  list = listr.split()
  string = ', '.join(list)
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Given a list of these items: " + string +
              """. Please provide me a possible recipes. 
              The very first line you should print should be the >Recipe Title<, so don't include ingredients.
              NOTE: You don't need to use all of the items listed below, but the more items used, the better.
              Use this format below for displaying the recipes, use g for grams, and number every instruction:
              Recipe Title: 
              Ingredients: 
              Instructions: 
              Calories: 
              Protein: 
              Carbs: 
              Fat: """,
    max_tokens=1024
  )
  chatgpt_response = response.choices[0].text.strip()
  # print(chatgpt_response)
  split = chatgpt_response.split(':')

  titlesplit = split[1].strip()
  ingredientsplit = split[2].strip()
  instructionsplit = split[3].strip()
  caloriesplit = split[4].strip()
  proteinsplit = split[5].strip()
  carbsplit = split[6].strip()
  fat = split[7].strip()

  title = titlesplit.split('\nIngredients')
  ingredients = ingredientsplit.split('\nInstructions')
  instructions = instructionsplit.split('\nCalories')[0]
  calorie = caloriesplit.split('\nProtein')[0]
  protein = proteinsplit.split('\nCarbs')[0]
  carbs = carbsplit.split('\nFat')[0]

  return title, ingredients, instructions, calorie, protein, carbs, fat

