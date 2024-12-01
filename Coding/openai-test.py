import openai
import os
from openai import OpenAI

API_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=API_key, organization= os.getenv("OPENAI_ORG_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)