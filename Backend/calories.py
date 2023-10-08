import openai
import datetime

openai.api_key = ("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")

# Get the current date
current_date = datetime.date.today()
formatted_date = current_date.strftime("%m/%d/%Y")

listr = input("Provide the ingredients that you have: ")
list = listr.split()
string = ', '.join(list)
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=f""""Given a list of these items: {string}
              onlytell me how long it takes before the product expires, in this format (1 day, 3 months, 2 years, etc)
              """,
  max_tokens=1024
)
chatgpt_response = response.choices[0].text.strip()

print(chatgpt_response)