from whapi import get_id, random_article, return_details, get_images, search

def wikihow(keyword): 
    print("placeholder")
    howresults = search(keyword, 1)
    print(howresults)
    howtitle = (dict(howresults[0]))['title']
    howid = (dict(howresults[1]))['article_id']
    howid = (dict(howresults[2]))['article_id']
    print(howtitle)



wikihow("cat")