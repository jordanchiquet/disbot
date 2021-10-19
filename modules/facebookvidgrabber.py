import requests
import re


def embedgrabber(url):
    html = requests.get(url)
    return(re.search('sd_src:"(.+?)"', html.text).group(1))