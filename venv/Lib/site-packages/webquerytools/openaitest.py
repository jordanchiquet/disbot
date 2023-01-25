import os
import openai

key = os.environ.get('OPENAI')

openai.api_key = key

#API OPENAI

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Wearing a brilliant striped hooded cloak of scarlet and black, and always wearing a different ornate mask from a seemingly limitless supply in his pack, the travelling poet, teacher, philosopher, and inventor Divine Nex is making his way through Navarene. You've heard the famous and faceless entertainer of a hundred faces was seeking escort to the town of Vesburgh, and for your own reasons, have decided to join him. You've been walking a while, and the first night which finds you all together approaches. Nex pours himself a glass of wine and retires to his large scarlet tent, leaving you all by the fire.\n\n Tl;dr",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['text'])