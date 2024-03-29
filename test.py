import requests
import bs4


class objavlenie:
    def __init__(self):
        self.price = None
        self.rooms = None
        self.square = None
        self.data = None
        self.url = None

    def attrs(self):
        return {
            'url': self.url,
            'rooms': self.rooms,
            'square': self.square,
            'data': self.data,
            'price': self.price
        }


objavlenies_list = []


def pars(html_text: bs4.element.Tag):
    cur = objavlenie()
    cur.url = html_text.find('a')['href']
    cur.rooms, cur.square = html_text.find('a').text.split(', ')
    cur.price = html_text.find('strong').text
    cur.data = html_text.find('div', class_='sr-2-item-date').text
    print(cur.attrs())


url0 = "https://avi.kz/almaty/nedvizhimost/prodazha-nedvizhimosti/prodazha-kvartir/vtorichnyy-rynok/"
responce = requests.get(url0)
html1 = bs4.BeautifulSoup(responce.text, "html.parser")
pages = len(html1.find_all("a", class_="j-pgn-page")) - 1
print(f'Всего страниц {pages}')

for i in range(pages):
    responce = requests.get(f"{url0}?lt=1&page={i+1}")
    # print(responce.status_code)
    html_page = bs4.BeautifulSoup(responce.text, 'html.parser')
    objavlenies = html_page.find_all("div", class_='sr-2-list-item-n-body')
    for i in objavlenies:
        # print(type(i))
        pars(i)
    # print(objavlenies)
