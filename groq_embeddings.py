from groq import Groq

client = Groq(
    api_key="",
)
response = client.embeddings.create(
messages=[
        {
  input:"Educative answers section is helpful",

  }
  ],
  model="text-embedding-ada-002",
  )


print(response.choices[0].message.content)