import openai

openai.api_key = ("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")

listr = input("Provide the ingredients that you have: ")
list = listr.split()
string = ', '.join(list)
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Given a list of these items: " + string +
            """. Please provide me a possible recipes. 
            The very first line you should print should be the >Recipe Title<, so don't include ingredients.
            NOTE: You don't need to use all of the items listed below, but the more items used, the better.
            Use this format below for displaying the recipes, and number every instruction:
            Recipe Title:
            Ingredients:
            Instructions:""",
  max_tokens=1024
)
chatgpt_response = response.choices[0].text.strip()
split = chatgpt_response.split(':')

titlesplit = split[1].strip()
ingredientsplit = split[2].strip()
instructions = split[3].strip()

title = titlesplit.split('\nIngredients')
ingredients = ingredientsplit.split('\nInstructions')

print(f"{title[0]}\n\n{ingredients[0]}\n\n{instructions}\n")