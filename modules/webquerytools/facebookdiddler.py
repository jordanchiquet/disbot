



import randomhelpers as rh
import requests
import os

fbkey = os.environ.get('FACEBOOKSECRET')

appid = "10229774072800241"

facebookUrl =   f"https://graph.facebook.com/{appid}"


headers = {'fields': 'friends',
            'debug': 'all',
            'access_token': fbkey}

try:
    r = requests.post(facebookUrl, headers=headers)
    print(r.content)
except Exception as e:
    rh.genErrorHandle(e)


