



def jokeTriggerMain(msgContent: str, serverid: int = 1):
    print("starting jokeTriggerMain")
    jokeTrigOut = (False, "")
    for key in jokeTriggerDict:
        if key in msgContent:
            jokeOut = jokeTriggerDict[key]
            jokeTrigOut = (True, jokeOut)
    for key in soloJokeTriggerDict:
        if key == msgContent:
            jokeOut = soloJokeTriggerDict[key]
            jokeTrigOut = (True, jokeOut)
    return(jokeTrigOut)


jokeTriggerDict = {
    "there's no need to fear": "UNDERDOG IS HERE",
    "hol up" : "https://youtu.be/kc9-HJ9Rd4w",
    "i get up" : "https://youtu.be/qjm9QZT06ig",
    "if it's meant to be" : "https://youtu.be/GihobUe-LSs",
    "speed me up" : "https://youtu.be/dCuCpVPkWDY",
}

soloJokeTriggerDict = {
    "computer": "yes?",
    "bad bot": ":(",
    "good bot": ":)",
    "holy fuck": "Wi Tu Lo",
    "too low": "Bang Ding Ow",
    "love": "is suicide",
    "what is your purpose": "input -> output",
    "speed me up": "https://youtu.be/dCuCpVPkWDY",
    "speed me down": "https://youtu.be/iALO4L166WU",
}

