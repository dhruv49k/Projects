import requests
from bs4 import BeautifulSoup

search = input("Enter Your City: ")
soup = BeautifulSoup(
    requests.get(f"https://www.google.com/search?q=weather+in+{search}").text,
    "html.parser",
)
# print(soup.prettify())
temperature = soup.find("div", div="BNeawe 18p41 AP7Wnd")
region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
day_and_whether_condition = soup.find("div", class_="BNeawe tAd8D AP7Wnd")
print(day_and_whether_condition.text)
print(region.text)
print(temperature.text)
