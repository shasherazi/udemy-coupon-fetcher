import requests
import time
from bs4 import BeautifulSoup


# List of webpages to scan for coupons
links = [f"https://www.discudemy.com/all/{i}" for i in range(1, 6)]
coupons = {}  # Dictionary of course names and their coupon codes

fileName = "coupons " + time.asctime().strip() + ".txt"

with open(fileName, "w+") as f:
    for link in links:
        response = BeautifulSoup(requests.get(link).text, "html.parser")
        aTags = response.find_all("a", class_="card-header")
        hrefs = [aTag.get("href") for aTag in aTags]  # hrefs of the aTags

        for href in hrefs:
            hrefResponse = BeautifulSoup(requests.get(href).text, "html.parser")
            # List of the href links of the buttons on the site that take you to the actual coupon code
            discButtons = hrefResponse.find_all("a", class_="discBtn")

            for discButton in discButtons:
                discButtonResponse = BeautifulSoup(
                    requests.get(discButton.get("href")).text, "html.parser"
                )
                coupons[
                    discButtonResponse.find("h1", class_="ui grey header").text
                ] = discButtonResponse.find("a", id="couponLink").text

                f.write(
                    discButtonResponse.find("h1", class_="ui grey header").text
                    + ": "
                    + discButtonResponse.find("a", id="couponLink").text
                    + "\n"
                )
                f.flush()  # Writes the link continuously to the file
