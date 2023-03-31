import openai
from config import OPENAI_KEY
from study_gpt import PRIMING_LIST
import random

subjects = ["fit and handsome Billionaire", "werewolf", "fit and handsome dragon men", "the son of a drug dealer", "the son of a president", "the son of a billionaire", "twins", "surrogate mother", "prince", "queen", "sugar daddy", "assistant"]
connection = ["one night stand", "pregnancy", "births", "abuse her", "funerals", "she sits on the bed in front of him", "put her legs apart", "they kiss", "she takes off her dress", "he splits the belt", "got very sick", "an unexpected meeting"]
place = ["bedroom with large bed", "luxury sportcar" "luxury penthouse and villa", "luxury penthouse", "Dark forest", "under the rain", "dark forest", "bathroom"]


openai.api_key = OPENAI_KEY



message_history = []

def ChatGPTCompletion():
    print("++++++++++")
    print(message_history)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )
    return completion


def add_message(message: str, role: str = "user") -> None:
    message_history.append({"role": role, "content": message})
    return


def create_mj_prompt():
    sub1 = subjects[random.randrange(0, len(subjects))]
    sub2 = subjects[random.randrange(0, len(subjects))]
    con = connection[random.randrange(0, len(connection))]
    pla = place[random.randrange(0, len(place))]
    final_prompt = "Make a detailed prompt for Midjourney v5 with next expression: " + sub1 + " and " + sub2 + ", " + con + ", background is " + pla

    for prime in PRIMING_LIST:
        add_message(prime)

    add_message(final_prompt)
    result_reply = ChatGPTCompletion()['choices'][0]['message']['content']
    if result_reply:
        message_history.clear()
        print("Message history cleared")
    return result_reply


print(create_mj_prompt())
