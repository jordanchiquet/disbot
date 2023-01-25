import TenGiphPy



#API TENOR
tenorget = TenGiphPy.Tenor(token='6S1DTQT40VGI')



def getgif(gifquery):
    gifurl = None
    gifjson = tenorget.search(gifquery)
    gifurl = gifjson['results'][0]['media'][0]['gif']['url']
    #with open('d:/renard/disbot/dognuts.json', 'w', encoding='utf-8') as f:
        #   json.dump(gifurl, f, ensure_ascii=False, indent=4)
    return(gifurl)
    #TODO: make None handler


