from craigslist import CraigslistHousing
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from util import post_listing_to_slack, in_boxes
from slackclient import SlackClient
import time
import settings

engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()


class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    geotag = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    location = Column(String)
    cl_id = Column(Integer, unique=True)
    area = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def parse_result(result):
    lat = 0
    lon = 0
    if 'geotag' in result:
        # Assign the coordinates.
        # NOTE THAT IT IS REVERSED
        lat = result["geotag"][1]
        lon = result["geotag"][0]
    else:
        result["area"] = ""

    # Try parsing the price.
    price = 0
    try:
        price = float(result["price"].replace("$", ""))
    except Exception:
        pass
    return Listing(
                link=result["url"],
                created=parse(result["datetime"]),
                lat=lat,
                lon=lon,
                name=result["name"],
                price=price,
                location=result["where"],
                cl_id=result["id"],
                area=result["area"]
            )


def scrape_area(area, category):
    """
    Scrapes craigslist for a certain geographic area, and finds the latest listings.
    :param area:
    :return: A list of results.
    """
    cl_h = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area=area, category=category,
                             filters={'max_price': settings.MAX_PRICE, "min_price": settings.MIN_PRICE})

    results = []
    gen = cl_h.get_results(sort_by='newest', geotagged=True, limit=50)
    for result in gen:
        listing = session.query(Listing).filter_by(cl_id=result["id"]).first()

        # Don't store the listing if it already exists.
        if listing is None and "where" in result and "geotag" in result:
            if result["where"] is None or not in_boxes(list(reversed(result['geotag'])), settings.BOXES):
                # If there is nothing identifying which neighborhood the result is from or geotag is not in boxes, skip
                continue
            listing = parse_result(result)
            # Save the listing so we don't grab it again.
            session.add(listing)
            session.commit()

            results.append(result)

    return results


def do_scrape():
    """
    Runs the craigslist scraper, and posts data to slack.
    """

    # Create a slack client.
    sc = SlackClient(settings.SLACK_TOKEN)

    # Get all the results from craigslist.
    all_results = []
    for area in settings.AREAS:
        for category in settings.CATEGORIES:
            all_results += scrape_area(area, category)

    print("{}: Got {} results".format(time.ctime(), len(all_results)))

    for result in all_results:
        if settings.SLACK_TOKEN != "":
            post_listing_to_slack(sc, result)
        print(result)


if __name__ == "__main__":
    do_scrape()
