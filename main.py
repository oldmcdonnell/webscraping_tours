import requests
import selectorlib


URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    #scrape the page source from the UTL
    reponse = requests.get(url)
    source = reponse.text
    return source

if __name__ == "__main__":
    print(scrape(URL))