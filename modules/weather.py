
from darksky.api import DarkSky, DarkSkyAsync #darksky_weather
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
            if userzip.isdigit() and len(userzip) < 6 and len(userzip) > 4:
                weatherzip = userzip
            else:
                return("invalid zip or something broken...")
        zipsearch = SearchEngine(simple_zipcode=True)
        zipresult = zipsearch.by_zipcode(int(weatherzip))
        city = zipresult.post_office_city
        wlat = zipresult.lat
        wlng = zipresult.lng
        darksky = DarkSky("7d2873772103272916b9cc1e357b6331")
        wbase = darksky.get_forecast(wlat, wlng, extend=False, lang=languages.ENGLISH, units = units.US,
                                        exclude=[weather.MINUTELY, weather.ALERTS])
        wsum = wbase.currently.summary
        wtemp = str(wbase.currently.temperature)[:2]
        wfeel = str(wbase.currently.apparent_temperature)[:2]
        wfore = wbase.daily.summary
        return(city + "|" + wsum + "|" + wtemp + "|" + wfeel + "|" + wfore)