import unittest
import json
from scraper import parse_result

class TestParse(unittest.TestCase):
    def test_get_results_from_craigslist_parses_correctly(self):
        # Here we're going to test the results of the dict from the craigslist library
        # Don't actually do the call to Craigslist
        # We mock it with reading from a json file
        with open('test_seattle_data.json', 'r') as f:
            data = json.load(f)
        # data is results

    def test_results_within_box_are_not_filtered(self):
        with open('test_seattle_data.json', 'r') as f:
            data = json.load(f)
        # We want to call find_point_of_interest



# def do_scrape():
#     cl = CraigslistHousing(site='toronto', area='tor', category='roo',
#                            filters={'max_price': 1500, 'min_price': 500})
#
#     results = cl.get_results(sort_by='newest', geotagged=True, limit=10)
#     for result in results:
#         print(result)
