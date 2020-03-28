from PIL import Image

import numpy as np 

def executeoverlay(imgpath):
    print("starting executeoverlay")
    dickshadow = Image.open("E:/disbot/picfolder/shadowdir/shadow.png")
    try:
        providedbackground = Image.open(imgpath)
        print("opened background")
        bgwidth, bgheight = providedbackground.size
        print("background image size: [" + str(bgwidth) + ", " + str(bgheight) + "]")
        dsresize = (bgwidth, bgheight)
        dickshadow = dickshadow.resize(dsresize, Image.ANTIALIAS)
        providedbackground.paste(dickshadow, (0, 0), dickshadow)
        providedbackground.save("E:/disbot/picfolder/shadowdir/dickshadow.png", "PNG")
        return("E:/disbot/picfolder/shadowdir/dickshadow.png")
    except:
        return("inv")



#     @bot.command()
# async def rev(ctx):
#     await ctx.send("Working on it...")
#     revquery = ctx.message.attachments[0].url
#     response = google_images_download.googleimagesdownload()
#     arguments = {"similar_images": revquery,"limit":1,"no_download":True}
#     revresult = response.download(arguments)
#     extractor = URLExtract()
#     for url in extractor.gen_urls(str(revresult)):
#         await ctx.send("Found this:\n" + url)