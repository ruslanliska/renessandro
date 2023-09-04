import logging
import random
from typing import Optional

import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from renessandro.config import OPENAI_KEY
from renessandro.openai_api.picture_data import picture

logger = logging.getLogger('server.openai_request')
openai.api_key = OPENAI_KEY

OPENAI_MODEL = 'gpt-3.5-turbo'


class ChatGPTHandler:
    """
    A handler for interacting with a chat-based language model (OPENAI_MODEL) for generating picture descriptions.

    This class provides methods for interacting with a chat-based language model, configured with an OpenAI API key
    and model name, to generate detailed picture descriptions. It includes a chat prompt template that can be used
    to request image generation based on user-defined prompts.

    Example Usage:
        handler = ChatGPTHandler()
    """
    def __init__(self):
        """
        Initialize a ChatGPTHandler instance with an OpenAI language model and a chat prompt template.

        This constructor initializes a ChatGPTHandler instance with the following components:
        - A chat-based language model (GPT-3) instance configured with the OpenAI API key and model name.
        - A chat prompt template that describes the Midjourney tool, its capabilities, and how to request image generation.
          This template includes placeholders for customizable image descriptions.

        Example Usage:
            handler = ChatGPTHandler()
        """
        self.llm = ChatOpenAI(openai_api_key=OPENAI_KEY, model_name=OPENAI_MODEL)
        template = """You are a helpful assistant which helps generate picture descriptions 
                      in details for Midjourney. Midjourney generates images from user prompts by adapting actual art 
                      styles to create an image of any combination of things desired. It excels at creating fantasy and 
                      sci-fi environments with dramatic lighting like rendered concept art from a video game. Midjourney
                      is an AI image generation tool that uses a Machine Learning (ML) algorithm trained on a large 
                      amount of image data to produce unique images. It is powered by Latent Diffusion Model (LDM), a 
                      cutting-edge text-to-image synthesis technique. LDMs are used to enable DM training on limited 
                      computational resources without compromising on quality and flexibility. This significantly 
                      improves visual fidelity. A cross-attention layer is introduced to the model architecture to turn 
                      the diffusion model into a powerful and flexible generator for generally conditioned inputs such 
                      as text and bounding boxes, enabling high-resolution convolution-based synthesis.
                      Please, generate me image with {subject_1} which looks like {subject_1_description} and {subject_2}
                      which looks like {subject_2_description} where they are doing action {action} which takes 
                      place in {place}. If there is nothing for subject_2, make up something only with subject_1.
                      Your work is to generate prompt for the midjourney which will create image based on your prompt. 
                      Avoid things which may violate sexual rules. Write just a prompt.
                      Here is some examples:
                        1) In a luxurious villa, a young and beautiful assistant female is seduced by her billionaire boss. He kisses her. She is wearing a dress. The composition is framed with a stunning view of the ocean in the background.
                        2) In a futuristic cityscape, a well fit cowboy holding a surrogate mother with a pregnancy test in her hand. They are standing on the rooftop of a skyscraper, with the cityscape as the background. The cowboy's rugged and weathered face bears a look of fierce determination and protectiveness, while the surrogate mother gazes up at him with a mixture of love and gratitude. The cowboy is wearing a black leather jacket, denim jeans, and a cowboy hat, while the surrogate mother is dressed in a white summer dress. The composition is skillfully captured to highlight the raw passion and intimacy between the two subjects, with the cityscape providing a dramatic and romantic backdrop.
                        3) A werewolf in good shape is holding his surrogate mother in his arms, while they stand on an island with a dark forest in the background. The werewolf is depicted as a humanoid wolf with muscular arms and sharp claws, while the surrogate mother is wearing a dress and has a pregnancy test in her hand. The pixel art is done in a retro 8-bit style, with vibrant colors and a detailed pixelated landscape. 
                        4) A muscular drug dealer with a scar on his cheek holding his assistant female against the wall in a luxury villa. His gaze is intense, and he kisses. The composition showcases the raw, dangerous power of the drug dealer against the opulent backdrop of the villa, creating a thrilling and sensual atmosphere.
                   """
        message = HumanMessagePromptTemplate.from_template(template=template)
        self.chat_prompt = ChatPromptTemplate.from_messages(messages=[message])

    def create_mj_prompt_default(self) -> str:
        """
        Create a default chat prompt for a chat-based language model (GPT-3) with random image data.

        This method generates a default chat prompt for a language model (GPT-3) by combining
        a base chat prompt template with random image data for subjects, actions, and places.

        Returns:
            str: The default chat prompt string for the language model.

        Example Usage:
            default_prompt = create_mj_prompt_default()
            response = llm(default_prompt.to_messages()).content.replace("\n", "")
        """
        chat_prompt_with_values = self.chat_prompt.format_prompt(**self.generate_image_data(image_data_type='default',))
        response = self.llm(chat_prompt_with_values.to_messages()).content.replace("\n", "")
        return response

    def create_mj_prompt_custom(self, **kwargs) -> str:
        """
        Create a custom prompt for a chat-based language model (GPT-3) with image data.

        This method generates a custom chat prompt for a language model (GPT-3) by combining
        a base chat prompt template with custom image data provided as keyword arguments.

        Args:
            **kwargs (dict): Custom image data for generating the prompt. Expected keys include:
                - 'subject_1': The primary subject.
                - 'subject_1_description': Description of the primary subject.
                - 'subject_2': The secondary subject (if applicable).
                - 'subject_2_description': Description of the secondary subject (if applicable).
                - 'action': The action in the image.
                - 'place': The location or place in the image.

        Returns:
            str: The custom chat prompt string for the language model.

        Example Usage:
            custom_prompt = create_mj_prompt_custom(
                subject_1='...', action='...', place='...')
            response = llm(custom_prompt.to_messages()).content.replace("\n", "")
        """
        chat_prompt_with_values = self.chat_prompt.format_prompt(**self.generate_image_data(image_data_type='custom',
                                                                                            **kwargs))
        response = self.llm(chat_prompt_with_values.to_messages()).content.replace("\n", "")
        return response

    @staticmethod
    def generate_image_data(image_data_type: str, **kwargs) -> dict[str, Optional[str]]:
        """
        Generate image data based on the specified type.

        This static method generates image data based on the provided 'image_data_type'.
        It can create custom image data using 'kwargs' or generate random image data for
        predefined attributes such as subjects, actions, and places when 'image_data_type'
        is set to 'default'.

        Args:
            image_data_type (str): The type of image data to generate ('custom' or 'default').
            **kwargs (dict): Additional keyword arguments for custom image data generation.

        Returns:
            dict: A dictionary containing image data with keys:
                - 'subject_1': The primary subject.
                - 'subject_1_description': Description of the primary subject.
                - 'subject_2': The secondary subject (if applicable).
                - 'subject_2_description': Description of the secondary subject (if applicable).
                - 'action': The action in the image.
                - 'place': The location or place in the image.

        Raises:
            AttributeError: If 'image_data_type' is not 'default' or 'custom'.

        Example Usage:
            custom_data = generate_image_data('custom', subject_1='...', action='...', place='...')
            default_data = generate_image_data('default')
        """
        if image_data_type == 'custom':
            return {
                'subject_1': kwargs.get('subject_1'),
                'subject_1_description': kwargs.get('subject_1_description'),
                'subject_2': kwargs.get('subject_2'),
                'subject_2_description': kwargs.get('subject_2_description'),
                'action': kwargs.get('action'),
                'place': kwargs.get('place'),
            }
        elif image_data_type == 'default':
            return {
                'subject_1': random.choice(picture.get('subject_1')),
                'subject_1_description': random.choice(
                    picture.get('subject_1_description')),
                'subject_2': random.choice(picture.get('subject_2')) if 'subject_2' in picture.keys() else None,
                'subject_2_description': random.choice(
                    picture.get('subject_2_description')) if 'subject_2_description' in picture.keys() else None,
                'action': random.choice(picture.get('action')),
                'place': random.choice(picture.get('place')),
            }
        else:
            raise AttributeError('Image data type must be default or custom.')

a = ChatGPTHandler()
print(a.create_mj_prompt_default())