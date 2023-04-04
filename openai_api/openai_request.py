import logging

import openai

from renessandro.config import OPENAI_KEY
from renessandro.openai_api.study_gpt import PRIMING_LIST

logger = logging.getLogger('server.openai_request')
openai.api_key = OPENAI_KEY


class ChatGPTHandler:
    def __init__(self):
        self.message_history = []

    def chat_GPT_completion(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
        )
        logger.info(completion)
        return completion

    def add_message(self, message: str, role: str = "user") -> None:
        self.message_history.append({"role": role, "content": message})
        return

    @classmethod
    def generate_prompt_for_niche(cls, niche: str) -> str:
        """
        Create random prompt for required niche from different subjects
        :param str niche: Niche for what creative prompt shall be generated
        :return str: prompt to ChatGPT for creation request to MJ
        """
        pass

    def create_mj_prompt(self, niche=None):
        for prime in PRIMING_LIST:
            self.add_message(prime)

        result_reply = self.chat_GPT_completion()['choices'][0]['message']['content']
        if result_reply:
            self.message_history.clear()
            logger.info('Message history cleared')
        return result_reply
