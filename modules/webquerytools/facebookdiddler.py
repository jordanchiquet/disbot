from pyfacebook import GraphAPI, FacebookApi



import randomhelpers as rh
import requests
import os




"""

curl -X GET 'https://graph.facebook.com/oauth/access_token
  ?client_id={your-app-id}
  &client_secret={your-app-secret}
  &grant_type=client_credentials'



Needs to take a url, determine if i is a valid facebook url. Determine if the page is publc. Determine if the page features media. Determine what kind of media that is. Return link to primary embedded video or image.

take a url 

determine if its valid for facebook 

determine if the page is public

determine if the page features media

determine what kind of media that is

return link to primary embedded video or image

nouns:
    url
    facebook
    page
    media
    video
    image
    link

facebookdiddler
    give url (variable)
    get page from url
    determine if page is public
    determine from page if page is media
        video
        image
        link            

"""
fb_secret = os.environ.get("FACEBOOKSECRET")
app_id = os.environ.get("FACEBOOKAPPID")

# fb_api = GraphAPI(access_token=fb_secret)
fb_api = FacebookApi(app_id=app_id, app_secret=fb_secret, application_only_auth=True)

userObject = fb_api.user.get_info(user_id="100090546786975")

print(userObject.first_name)

fb_api.page.get_info(page_id="20531316728")

fb_api.page.get_info(page_id="616104607192359")



# fb_api.user.get_info(user_id="413140042878187")

#https://www.facebook.com/photo.php?fbid=616104607192359&set=a.451536976982457&type=3&is_lookaside=1



def facebook_diddler(url) -> str:
    print(f"facebook_diddler func started with url [{url}]")
    page = requests.get(url)
    page_valid, page_valid_msg = page_verifier(page)

    # page verifier will check if the page is valid, if the page is facebook, if the page is public, and if the page is media

def page_verifier(page: object) -> tuple:
    print(f"page_verifier func started with page [{page}]")
    if page.status_code == 200:
        print(f"Response okay for [{page.url}]")
    else:
        return False, f"Response [{page.status_code}] for [{page.url}]"
    if "facebook.com" not in page.headers["report-to"]:
        return False, f"Page is not facebook [{page.url}]"
    #todo: check if page is public or private... not sure how to do this yet

    # probably have to give in and use the facebook api to get this info. maybe there is a good wrapper already out there
    print(page.headers) 
    return(True, "placeholder")




fbtest = "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100063584760907"
# facebook_diddler(fbtest)




