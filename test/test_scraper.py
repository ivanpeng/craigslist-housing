import unittest
import json
from util import in_box, in_boxes


class TestParse(unittest.TestCase):
    def test_get_results_from_craigslist_parses_correctly(self):
        # Here we're going to test the results of the dict from the craigslist library
        # Don't actually do the call to Craigslist
        # We mock it with reading from a json file
        with open('test/test_seattle_data.json', 'r') as f:
            data = json.load(f)
        # data is results

    def test_results_within_box_are_not_filtered(self):
        with open('test/test_seattle_data.json', 'r') as f:
            data = json.load(f)
        # We want to call in_box
        #
        greenwood_listing = data[0]
        self.assertEqual("6752686752", greenwood_listing['id'])
        box = [[-122.43275,47.654607], [-122.265588,47.75539]]
        geotag = list(reversed(greenwood_listing['geotag']))
        self.assertTrue(in_box(geotag, box))
        fake_box = [[-122.726126,47.538689], [-122.558963,47.639696]]
        self.assertFalse(in_box(geotag, fake_box))

    def test_results_is_within_at_least_one_dict_of_boxes(self):
        with open('test/test_seattle_data.json', 'r') as f:
            data = json.load(f)
        greenwood_listing = data[0]
        geotag = list(reversed(greenwood_listing['geotag']))
        box = [[-122.43275,47.654607], [-122.265588,47.75539]]
        fake_box = [[-122.726126,47.538689], [-122.558963,47.639696]]
        d = {"invalid_area": fake_box, "valid_area": box}
        self.assertTrue(in_boxes(geotag, d))


# def do_scrape():
#     cl = CraigslistHousing(site='toronto', area='tor', category='roo',
#                            filters={'max_price': 1500, 'min_price': 500})
#
#     results = cl.get_results(sort_by='newest', geotagged=True, limit=10)
#     for result in results:
#         print(result)
