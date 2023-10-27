import openai
import os
import modules.randomhelpers as rh


key = os.environ.get('OPENAI')

openai.api_key = key
#API OPENAI

def getdalle(prompt):

    try:
        modresponse = openai.Moderation.create(input=prompt, model="text-moderation-latest")
        print(modresponse)
        flagged = modresponse["results"][0]["flagged"]
        if not flagged:
            print("got false")
            response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
            print("test line")
            image_url = response['data'][0]['url']
            print(image_url)
        else:
            image_url = f"error, your prompt {prompt} was MODERATED by openAI\n" + f"{modresponse['results'][0]['categories']}"
    except Exception as e:
        image_url = f"error - {prompt}| OpenAI just returned the following to Renard: **'{(rh.genErrorHandle(e)).split('InvalidRequestError:')[1]}'**"
    finally:
        print("returning")
        return(image_url)
