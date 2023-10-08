import openai
import datetime
import os
import re

def expire(listr):

    openai.api_key = (os.environ["OPENAI_KEY"])

    # Get the current date
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%m/%d/%Y")

    string = ', '.join(listr)
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f""""What is the shelf life of these items: {string}\n
                Take your time and figure out what the shelf life of each item is.\n
                If I bought these items on {formatted_date}, on what day would they expire\n
                Do it in mm/dd/yyyy format, and print it out like a python dictionary (NOTE: DON'T GIVE A DATE FROM THE PAST):\n    
                Use this format to print it out: [item]:mm/dd/yyyy 
                """,
    max_tokens=1024
    )
    chatgpt_response = re.split(":|\n",response.choices[0].text.strip())

    return chatgpt_response