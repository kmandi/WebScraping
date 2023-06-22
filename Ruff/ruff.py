import requests
from bs4 import BeautifulSoup

url = "https://beta.ruff.rs/docs/rules/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


s1 = soup.find('div', class_="md-container")
s2 = s1.find('div', class_="md-main__inner md-grid")
s3 = s2.find('div', class_="md-content")
s4 = s3.find('article', class_="md-content__inner md-typeset").get_text()
# s5 = s4.find_all('div', attrs={'class': 'typeset__scrollwrap'})

# for s in s4.find_all('h2'):
#     print(s.text)


# s = soup.find_all('div', attrs={'class': 'md-typeset__scrollwrap'})
print(len(s4))
# print(s[0])
for i in s4:
    print(i)