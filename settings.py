import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 600

# The maximum rent you want to pay per month.
MAX_PRICE = 1500

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'seattle'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["see"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "wallingford 1": [[-122.343485,47.64021],[-122.296369,47.670357]],
    "wallingford 2":[[-122.356014,47.635787],[-122.324445,47.653725]],
    "wallingford 3": [[-122.338289,47.664418], [-122.30672,47.682346]],
    "fremont": [[-122.354252,47.654089],[-122.322683,47.67202]],
    "portage bay": [[-122.330962,47.634891],[-122.299393,47.652829]]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["university district", "u district", "wallingford", "tangletown", "fremont", "montlake", "eastlake", "portage bay", "queen anne", "meridian", ""]

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
#CRAIGSLIST_HOUSING_SECTION = 'apa'
CATEGORIES = ["apa", "roo"]

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#seattle-housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    import private
    SLACK_TOKEN = private.SLACK_TOKEN
    print("Slack token imported from private settings file.")
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass