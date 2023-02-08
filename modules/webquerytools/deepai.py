import requests
import os

deepaikey = os.environ.get("DEEPAI")


def generateImage(query):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text':query
        },
        headers={'api-key': deepaikey}
    )
    if r.status_code == 200:
        return r.json()["output_url"]
    else:
        return f"Error: {r.status_code} {r.reason} {r.text}"


generateImage("hello world")