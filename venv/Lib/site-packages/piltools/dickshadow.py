from PIL import Image #Pillow
import os



def executeoverlay(bgpath, fgpath: str = ("/home/ubuntu/disbot/picfolder/shadowdir/shadow.png")):
    print("starting executeoverlay")
    dickshadow = Image.open(fgpath)
    finalimg = "/home/ubuntu/disbot/picfolder/shadowdir/dickshadow.png"
    # if os.exists(finalimg): this did not work
    #     os.remove(finalimg)
    try:
        providedbackground = Image.open(bgpath)
        print("opened background")
        bgwidth, bgheight = providedbackground.size
        print("background image size[" + str(bgwidth) + ", " + str(bgheight) + "]")
        dsresize = (bgwidth, bgheight)
        dickshadow = dickshadow.resize(dsresize, Image.ANTIALIAS)
        providedbackground.paste(dickshadow, (0, 0), dickshadow)
        print("pasting suceeded")
        providedbackground.save("/home/ubuntu/disbot/picfolder/shadowdir/dickshadow.png", "PNG")
        print("saving suceeded")
        return("/home/ubuntu/disbot/picfolder/shadowdir/dickshadow.png")
    except:
        return("inv")