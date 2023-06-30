from instascrape import *


google_last_posturl = 'https://www.instagram.com/p/Cr3PR8yOOqB/'


def instacrape_media_grabber(url):
    headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=35821516%3AQJrybWhh2gXl3u%3A6%3AAYdHIMjK-IDWfbc-cQnr2NfY2-nbZftNgjHexz2ZzQ;"
    }

    post = Post(url)
    post.scrape(headers=headers)
    # profile = Profile(url)
    # profile.scrape(headers=headers)
    # print(profile.flat_json_dict)

instacrape_media_grabber("https://www.instagram.com/p/Cr3PR8yOOqB/")
# instacrape_media_grabber("https://www.instagram.com/google/")


def post_media_grabber(url):
    if "https://" in url:
        slash_media_index = 5
        prefix = ""

        
    else:
        slash_media_index = 3
        prefix = "https://"
    ready_for_media_url = "/".join(url.split("/")[:slash_media_index])
    media_url = prefix + ready_for_media_url + "/media/?size=l"
    print(media_url)

def reel_media_grabber(url):
    pass




