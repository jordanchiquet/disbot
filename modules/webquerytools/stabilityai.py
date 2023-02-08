import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

stability_api = client.StabilityInference(
    key=os.environ.get("STABILITYAI"),
    verbose=True,
    engine="stable-diffusion-v1-5"
)

def generateStable(query):
    answers = stability_api.generate(
        prompt=query,
        steps=30,
        cfg_scale=8.0,
        width=512,
        height=512,
        samples=1
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
                return(f"error: content/booby error i have not gotten around yet sorry (prompt was: {query})")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                try:
                    img.save(f"stablediffresult.png")
                except IOError:
                    print("cannot save image")
    return("success")




