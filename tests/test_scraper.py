import sys
from craigslist import CraigslistHousing
from scraper import parse_result


def do_scrape():
    cl = CraigslistHousing(site='toronto', area='tor', category='roo',
                           filters={'max_price': 1500, 'min_price': 500})

    results = cl.get_results(sort_by='newest', geotagged=True, limit=10)
    for result in results:
        print(result)
