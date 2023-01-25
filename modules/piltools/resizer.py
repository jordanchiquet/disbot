from PIL import Image

def pilResizer(imgpath: str, x: int, y: int):
    pass
    #allow option for percentage instead maybe, or just provide one and maintain ratio

from os import listdir
import requests 





source_directory = sys.argv[1]
new_directory = sys.argv[2]




images = [f for f in listdir(source_directory) if f.startswith("ic_")]

for image in images:
        source_image = Image.open(source_directory + image)
        new_image = source_image.rotate(-90).resize(128, 128).convert("RGB")
        new_image.save(new_directory + file, "JPEG")


response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))


response = requests.get(url)
response.raise_for_status()