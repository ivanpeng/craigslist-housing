import sys
from craigslist import CraigslistHousing

cl = CraigslistHousing(site='toronto', area='tor', category='apa',
                       filters={'max_price': 1500, 'min_price': 750})

results = cl.get_results(sort_by='newest', geotagged=True, limit=20)
for result in results:
    print(result)
