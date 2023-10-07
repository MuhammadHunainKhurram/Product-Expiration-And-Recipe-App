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
            Use this format below for displaying the recipes:
            Recipe Title:

            Ingredients:

            Instructions in Numerical Order:""",
  max_tokens=100
)
print(response.choices[0].text.strip())
