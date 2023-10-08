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
              Use the website eatbydate.com to give an estimated expiration date using the current date: {formatted_date} as a guideline.
              Example: If a product has a shelf life of 3 days, and today is 10/07/2023, it will print out 10/10/2023, depending on what day it is.
              Do it in mm/dd/yyyy format, but print it out like a python dictionary:
              [item] [take your time thinking about the expiration date, don't rush it]:mm/dd/yyyy 
              """,
  max_tokens=1024
)
chatgpt_response = response.choices[0].text.strip()

print(chatgpt_response)