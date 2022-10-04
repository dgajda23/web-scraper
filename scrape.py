from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_float_price:from%5D=1000&search%5Bfilter_float_price:to%5D=1500").text

soup = BeautifulSoup(source, "lxml")

csv_file = open("olx_scrape.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Date", "Price", "Link"])


for div in soup.find_all("div", {"data-cy": "l-card"}):

  url = div.find('a', href=True)['href']
  if "otodom.pl" in url:
    urlBase = ""
  else:
    print("HERE")
    urlBase = "https://www.olx.pl"
  fullUrl = urlBase + url

  print(fullUrl)

  listingTitle = div.find('h6', {"class": "css-1pvd0aj-Text eu5v0x0"}).text
  print("Title: " + listingTitle)

  listingDate = div.find("p", {"class": "css-p6wsjo-Text eu5v0x0"}).text
  print("Date: " + listingDate)

  listingPrice = div.find({"p"}, {"data-testid": "ad-price"}, {"class": "css-1q7gpp-Text eu5v0x0"}).text
  print("Price: " + listingPrice)

  print()

  csv_writer.writerow([listingTitle, listingDate, listingPrice, fullUrl])

csv_file.close()

