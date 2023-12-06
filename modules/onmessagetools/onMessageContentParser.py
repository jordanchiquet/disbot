from modules import randomhelpers as rh


def onMessageContentParserMain(msgObject: any):
    if msgObject.embeds:
        print("embed exists")
        # determineEmbedType(msgObject.embeds[0])
    return containsEmbed(msgObject)

def containsEmbed(msgobj) -> bool:
    if msgobj.embeds:
        print("embed exists")
        return True
    else:
        print(msgobj.content)
        print("embed doesn't exist")
        return False

def setObjectImage(embed) -> bool:
    pass

# good to know but don't think I need the type actually. 

# def determineEmbedType(embed):
#     print(f"""
#     embed.description: [{embed.description}]
#     embed.thumbnail: [{embed.thumbnail}]
#     embed.image: [{embed.image}]
#     embed.video: [{embed.video}]
#     """)
#     if embed.image:
#         print("embed image exists")
#         #if only image, only this fires
#     else:
#         print("embed image doesn't exist")
#     if embed.thumbnail:
#         print("embed thumbnail exists")
#     else:
#         print("embed thumbnail doesn't exist")
#     if embed.video:
#         print("embed video exists")
#         #if only video, only this fires
#     else:
#         print("embed video doesn't exist")
    