import requests
from bs4 import BeautifulSoup
import csv

# pages we are scraping (investing.com United States 30)
stocks = ["https://www.investing.com/equities/3m-co",
          "https://www.investing.com/equities/american-express",
          "https://www.investing.com/equities/amgen-inc",
          "https://www.investing.com/equities/apple-computer-inc",
          "https://www.investing.com/equities/boeing-co",
          "https://www.investing.com/equities/caterpillar",
          "https://www.investing.com/equities/chevron",
          "https://www.investing.com/equities/cisco-sys-inc",
          "https://www.investing.com/equities/coca-cola-co",
          "https://www.investing.com/equities/dow-chemical",
          "https://www.investing.com/equities/goldman-sachs-group",
          "https://www.investing.com/equities/home-depot",
          "https://www.investing.com/equities/honeywell-intl",
          "https://www.investing.com/equities/ibm",
          "https://www.investing.com/equities/intel-corp",
          "https://www.investing.com/equities/johnson-johnson",
          "https://www.investing.com/equities/jp-morgan-chase",
          "https://www.investing.com/equities/mcdonalds",
          "https://www.investing.com/equities/merck---co",
          "https://www.investing.com/equities/microsoft-corp",
          "https://www.investing.com/equities/nike",
          "https://www.investing.com/equities/procter-gamble",
          "https://www.investing.com/equities/salesforce-com",
          "https://www.investing.com/equities/the-travelers-co",
          "https://www.investing.com/equities/united-health-group",
          "https://www.investing.com/equities/verizon-communications",
          "https://www.investing.com/equities/visa-inc",
          "https://www.investing.com/equities/walgreen-co",
          "https://www.investing.com/equities/wal-mart-stores",
          "https://www.investing.com/equities/disney"
          ]

# open csv file
file = open("stocks.csv", "w")
writer = csv.writer(file)
writer.writerow(["Company", "Price", "Change"])

# scrape each stock's page
for stock in stocks:
    # initialize the html parser
    page = requests.get(stock)
    soup = BeautifulSoup(page.text, "html.parser")

    # get the company name, stock price, and percentage change
    company = soup.find("h1", {"class": "text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2"}).text
    price = soup.find("div", {"class": "instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold"
                              }).find_all('span')[0].text
    change = soup.find("div", {"class": "instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold"
                               }).find_all('span')[2].text

    # print a status message to the terminal
    print("Loading: ", stock)
    print(company, "-", price, "-", change)

    # write the data to the csv
    writer.writerow([company.encode("utf-8"), price.encode("utf-8"), change.encode("utf-8")])

file.close()
