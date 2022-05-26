from PIL import Image #Pillow

import numpy as np 

def executeoverlay(imgpath):
    print("starting executeoverlay")
    dickshadow = Image.open("/home/ubuntu/disbot/picfolder/shadowdir/shadow.png")
    try:
        providedbackground = Image.open(imgpath)
        print("opened background")
        bgwidth, bgheight = providedbackground.size
        print("background image siz/home/ubuntu [" + str(bgwidth) + ", " + str(bgheight) + "]")
        dsresize = (bgwidth, bgheight)
        dickshadow = dickshadow.resize(dsresize, Image.ANTIALIAS)
        providedbackground.paste(dickshadow, (0, 0), dickshadow)
        providedbackground.save("/home/ubuntu/disbot/picfolder/shadowdir/dickshadow.png", "PNG")
        return("/home/ubuntu/disbot/picfolder/shadowdir/dickshadow.png")
    except:
        return("inv")