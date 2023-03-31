import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "In what yer the WW2 started?"},
    ]
)

reply_content = completion['choices'][0]['message']['content']

message_history = []
