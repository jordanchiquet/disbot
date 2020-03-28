from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from msrest.authentication import CognitiveServicesCredentials
from modules.googleimageapi import imageget

def bingimage(query):
    subscription_key = "bb109905a4fc4b728f2c85dd32745cb8"
    subscription_endpoint = "https://realdisbotimageres.cognitiveservices.azure.com/bing/v7.0/search?q="
    search_term = query

    client = ImageSearchClient(endpoint=subscription_endpoint, credentials=CognitiveServicesCredentials(subscription_key))

    image_results = client.images.search(query=search_term)

    if image_results.value:
        first_image_result = image_results.value[0]
        print("Total number of images returned: {}".format(len(image_results.value)))
        print("First image thumbnail url: {}".format(
            first_image_result.thumbnail_url))
        return(first_image_result.content_url)
    else:
        print("no bing image result, fowarding to google")
        googletry = imageget(query)
        return(googletry)