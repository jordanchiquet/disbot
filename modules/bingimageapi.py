from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from modules.googleimageapi import imageget
from msrest.authentication import CognitiveServicesCredentials
import random

def bingimage(query):
    try:
        subscription_key = "bb109905a4fc4b728f2c85dd32745cb8"
        subscription_endpoint = "https://realdisbotimageres.cognitiveservices.azure.com/bing/v7.0/search?q="
        search_term = query

        client = ImageSearchClient(endpoint=subscription_endpoint, credentials=CognitiveServicesCredentials(subscription_key))

        image_results = client.images.search(query=search_term, safe_search="Off")

        if image_results.value:
            first_image_result = image_results.value[0]
            print("Total number of images returned: {}".format(len(image_results.value)))
            print("First image thumbnail url: {}".format(
                first_image_result.thumbnail_url))
            return(first_image_result.content_url)
        else:
            return("No image results returned!")
    except:
        print("bing just failed to get an image, trying google...")
        return(imageget(query))
