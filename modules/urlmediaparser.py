# Check if input string has a url from a list of url types
# If it does, try to get the embeddable media from the url and return it
# If it doesn't, return None
# example instagram url: https://www.instagram.com/reel/Cq6f-U7Mcyq/?igshid=YmMyMTA2M2Y=
# example tiktok url: https://www.tiktok.com/t/ZTR3LY54U/

from modules import randomhelpers as rh

import urllib.request
from urllib.error import HTTPError, URLError


def getEmbeddableMediaFromUrl(input: str) -> str:
    print(f"getEmbeddableMediaFromUrl started with input: [{input}]")
    embeddableMedia = None
    if rh.getRegexReturn(query=r"https://www.instagram.com/reel/", input=input) is not None:
        embeddableMedia = getEmbeddableMedia(input, "instagram reel")
    elif rh.getRegexReturn(query=r"https://www.tiktok.com/t/", input=input) is not None:
        embeddableMedia = getTiktokEmbeddableMedia(input)
    return(embeddableMedia)

def getEmbeddableMedia(input: str, mediaType: str) -> str:
    print(f"getEmbeddableMedia started with input: [{input}] and mediaType: [{mediaType}] + ")
    embeddableMedia = None
    if mediaType == "instagram reel":
        embeddableMedia = getInstagramReelEmbeddableMedia(input)
    return(embeddableMedia)

websourcetest = rh.getWebSourceHTML("https://www.instagram.com/reel/Cq6f-U7Mcyq/?igshid=YmMyMTA2M2Y=")


#.title gives me the comments
print(websourcetest.title)
