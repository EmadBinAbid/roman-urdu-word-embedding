""""
@author: Emad Bin Abid
@date: 31-10-2018
"""

### Program to scrap a website to obtain roman-urdu words

## Dependencies
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# URLs
url = "https://jang.com.pk/roman/news/"

# url1 = "https://jang.com.pk/roman/news/8272"
# url2 = "https://jang.com.pk/roman/news/8271"
# url3 = "https://jang.com.pk/roman/news/8270"

database = []

def scraper(url, html_tag, attrs={}):
    uClient = uReq(url)
    page_html = uClient.read()      # Reading HTML from the URL
    uClient.close()

    page_soup = soup(page_html, "html.parser")      # Parsing the HTML
    container = page_soup.findAll(html_tag, attrs)
    return container

def add_to_database(container):
    for i in container:
        database.append(i)

def init_clean():
    # Initial cleaning database
    database.pop()
    for i in range(len(database)):
        try:
            database[i] = database[i].text      # Removing tag names
        except:
            print("[-]ERROR: Could not clean entry=",i)
    try:
        if '' in database:
            database.remove('')
    except:
        print("[-]ERROR: Could not remove ''")

def display():
    # Printing entries
    for i in range(len(database)):
        print(database[i])


# Calling functions
# add_to_database(scraper(url1, "p"))
# add_to_database(scraper(url2, "p"))
# add_to_database(scraper(url3, "p"))

print("[...]: Processing, please wait...")
for qNum in range(4700, 5000):
    try:
        add_to_database(scraper(url+str(qNum), "p"))
        print("[+]SUCCESS:", url+str(qNum), "scraped successfully!")
    except:
        print("[-]ERROR: Could not scrape", url + str(qNum))

print("[+]SUCCESS: Done scraping!")
print("[...]: Init cleaning...")
init_clean()
print("[+]SUCCESS: Done init cleaning!")

print("[...]: Writing to File...")
file = open("../data/database.txt", "a+")
for i in range(len(database)):
    try:
        file.write(database[i])
        file.write('\n')
    except:
        print("[-]ERROR: Could not write to file at entry=",i)
file.close()

print("[+]SUCCESS: Writing to File completed successfully!")

print()
print("---------")
print("DATABASE:")
print("---------")
# display()

# print(database)


print("LENGTH OF DATABASE=", len(database))