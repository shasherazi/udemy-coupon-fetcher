import requests
from bs4 import BeautifulSoup


link = "https://www.discudemy.com/all"
response = BeautifulSoup(requests.get(link).text, "html.parser")

# List of the links on the cards on the site
aTags = response.find_all("a", class_="card-header")
hrefs = [aTag.get("href") for aTag in aTags]  # hrefs of the aTags

discButtons = []  # List of the href links of the buttons on the site that take you to the actual coupon code
coupons = {}  # Dictionary of the course names and their coupon codes

for href in hrefs:
    link = href
    hrefResponse = BeautifulSoup(requests.get(link).text, "html.parser")
    discButtons.append(hrefResponse.find("a", class_="discBtn").get("href"))

for discButton in discButtons:
    link = discButton
    discButtonResponse = BeautifulSoup(requests.get(link).text, "html.parser")
    coupons[discButtonResponse.find(
        "h1", class_="ui grey header").text] = discButtonResponse.find("a", id="couponLink").text

with open("coupons.txt", "w") as f:
    for courseName, couponLink in coupons.items():
        f.write(courseName + ": " + couponLink + "\n")
