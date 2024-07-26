import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')

#openai.api_key = "somekey"
#openai.base_url = "http://localhost:3040/v1/"

response = openai.Embedding.create(
  input="Educative answers section is helpful",
  model="text-embedding-ada-002"
  #model="gpt-3.5-turbo"
)

print(response)