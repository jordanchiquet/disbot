
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from modules.renardusers import renardusers
from uszipcode import SearchEngine


def weatherget(userid, userzip: str = None, register: bool = False):
    userinit = renardusers(userid, "zip", userzip)
    if register:
        if userzip.isdigit() and len(userzip) < 6 and len(userzip) > 4:
            userinit.userwrite()
            return("new zip registered!")
        else:
            return("invalid zip or something broken...")
    else:
        if userzip is None:
            print("userzip none")
            result = userinit.userread()
            if result is None:
                return("no zip set for you... provide one for one time use or set one for future use")
            else:
                weatherzip = result[0]
        else:
            if userzip.isdigit() and len(userzip) == 5:
                weatherzip = userzip
            else:
                return("invalid zip or something broken...")
        print("starting weather search with zip : [" + weatherzip + "]")
        zipsearch = SearchEngine(simple_zipcode=True)
        zipresult = zipsearch.by_zipcode(int(weatherzip))
        city = zipresult.post_office_city
        print(city)
        wlat = zipresult.lat
        print(wlat)
        wlng = zipresult.lng
        print(wlng)
        print("made it to darksky api provision")
        darksky = DarkSky("e18c5cc67731e2f871a8283a4bfaf1f5")
        wbase = darksky.get_forecast(wlat, wlng, extend=False, lang=languages.ENGLISH, units = units.US)
        print("got forecast")
        wsum = wbase.currently.summary
        wtemp = str(wbase.currently.temperature)[:2]
        wfeel = str(wbase.currently.apparent_temperature)[:2]
        wfore = wbase.daily.summary
        returnstr = city + "|" + wsum + "|" + wtemp + "|" + wfeel + "|" + wfore
        print("weather return string: [" + returnstr + "]")
        return(returnstr)