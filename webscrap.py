import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/mobile-phones-big-saving-days-jan23-56hj-store?param=16&fm=neo%2Fmerchandising&iid=M_8fe2d626-a69c-4169-a966-8ba40660dc4d_1_8ZPR8BP0RP3K_MC.BYIXDBQAWBHQ&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles%2B%2526%2BTablets_BYIXDBQAWBHQ&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=BYIXDBQAWBHQ"

response = requests.get(url)
htmlCnt = response.content
soup = BeautifulSoup(htmlCnt, "html.parser")

# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.find_all('p'))
# print(soup.find(id="next-page-link-tag"))
# print(soup.find_all('a'))

# get all href link.
# for lnk in soup.find_all('a'):
#     print(lnk.get('href'))

# get all image link.
# for i in soup.find_all('img'):
    # print(i.get('src'))

# get all using class name.
# product_1 = soup.find_all('div', class_='_3ply-c row')
# print(product_1)

# product_2 = soup.find('div', attrs={'class': '_3pLy-c'})
# print(product_2)
