import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = openai.OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant to help me give me key word from my input."},
    {"role": "user", "content": "Play Taylor Swift's latest album?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)