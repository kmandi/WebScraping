import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts"

response = requests.get(url)
htmlCnt = response.content
soup = BeautifulSoup(htmlCnt, "html.parser")

titles = []
prices = []
images = []


for i in soup.find_all('div', attrs={'class': '_1xHGtK _373qXS'}):

    # title data stor.
    title = i.find('a', attrs={'class': 'IRpwTa'})
    titles.append(title.string)

    #price data stor.
    p1 = i.find('a', attrs={'class': '_3bPFwb'})
    p2 = p1.find('div', attrs={'class': '_25b18c'})
    p3 = p2.find('div', attrs={'class': '_30jeq3'})
    price = p3.string
    prices.append(price[1:])

    #image data stor.
    im1 = i.find('img', attrs={'class': '_2r_T1I'})
    images.append(im1.get('src'))

print(titles)
print()
print(prices)
print()
print(images)