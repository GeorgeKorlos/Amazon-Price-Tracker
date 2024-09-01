import requests
from bs4 import BeautifulSoup
import os
import smtplib

ADDRESS = os.getenv('ADRS')
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')
URL = os.getenv('URL')
USER_AGENT = os.getenv('USER_AGENT')
LANG = os.getenv('LANG')

headers = {
    'User-Agent': USER_AGENT,
    'Accept-Language': LANG
}

response = requests.get(url=URL, headers=headers)
page = response.text
soup = BeautifulSoup(page,'lxml')
price = soup.find(name='span', class_='a-offscreen').getText().split('$')[1]
price = price.replace(',', '')
new_price = float(price)

title = soup.find(id='productTitle').get_text().strip()

BUY = 1500

if new_price < BUY:
    msg = f'{title} is on sale for {new_price}'

    with smtplib.SMTP(ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject:Amazon Price Alert!\n\n{msg}\n{URL}'.encode('utf-8')
        )