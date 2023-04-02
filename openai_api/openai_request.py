import logging

import openai
from renessandro.config import OPENAI_KEY
from renessandro.openai_api.study_gpt import PRIMING_LIST
import random

logger = logging.getLogger('server.openai_request')

subjects = ["fit and handsome Billionaire", "werewolf", "fit and handsome dragon men", "the son of a drug dealer", "the son of a president", "the son of a billionaire", "twins", "surrogate mother", "prince", "queen", "sugar daddy", "assistant"]
connection = ["one night stand", "pregnancy", "births", "abuse her", "funerals", "she sits on the bed in front of him", "put her legs apart", "they kiss", "she takes off her dress", "he splits the belt", "got very sick", "an unexpected meeting"]
place = ["bedroom with large bed", "luxury sportcar" "luxury penthouse and villa", "luxury penthouse", "Dark forest", "under the rain", "dark forest", "bathroom"]

profession_list = ['chef', 'artist', 'athlete', 'librarian', 'football player', 'policeman']
process_list = ['cooking', 'painting', 'running', 'organizing books', 'reading', 'cleaning']
place_list = ['restaurant kitchen', 'art studio', 'stadium', 'library', 'forest', 'city center']


openai.api_key = OPENAI_KEY


message_history = []


def ChatGPTCompletion():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )
    logger.info(completion)
    return completion


def add_message(message: str, role: str = "user") -> None:
    message_history.append({"role": role, "content": message})
    return

def generate_prompt_for_niche(niche: str) -> str:
    """
    Create random prompt for required niche from different subjects
    :param str niche: Niche for what creative prompt shall be generated
    :return str: prompt to ChatGPT for creation request to MJ
    """
    pass


def create_mj_prompt():
    sub1 = profession_list[random.randrange(0, len(profession_list))]
    sub2 = profession_list[random.randrange(0, len(profession_list))]
    con = process_list[random.randrange(0, len(process_list))]
    pla = place_list[random.randrange(0, len(place_list))]
    final_prompt = "Make a detailed prompt for Midjourney v5 with next expression: " + sub1 + " and " + sub2 + ", " + con + ", background is " + pla
    logger.info(f"Final prompt: {final_prompt}")
    for prime in PRIMING_LIST:
        add_message(prime)

    add_message(final_prompt)
    result_reply = ChatGPTCompletion()['choices'][0]['message']['content']
    if result_reply:
        message_history.clear()
        logger.info('Message history cleared')
    return result_reply

