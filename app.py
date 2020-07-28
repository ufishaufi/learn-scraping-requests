import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/monthly.php?=308'

contents = requests.get(url)
# print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]
# print(data)

sholat = {}
d = 0
for i in data:
    # print(i.get_text())
    if d == 1:
        sholat['shubuh'] = i.get_text()
    elif d == 2:
        sholat['dzuhur'] = i.get_text()
    elif d == 3:
        sholat['ashar'] = i.get_text()
    elif d == 4:
        sholat['maghrib'] = i.get_text()
    elif d == 5:
        sholat['isya'] = i.get_text()
    d += 1

print(sholat)

print(f"Shalat ashar menujukkan jam: {sholat['ashar']} WIB")
