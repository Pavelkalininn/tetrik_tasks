
import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://ru.wikipedia.org/'


def counter():
    url = DOMAIN + 'w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90'
    animals = {}
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        next_page = soup.find_all(
            'a', class_="", text='Следующая страница')[-1].get('href')
        categories = soup.find_all('div', class_="mw-category-group")[2:]
        for category in categories:
            category_char = category.find('h3').text

            if category_char == 'A':
                return animals

            if category_char in animals:
                animals[category_char] += list(
                    this.get('title') for this in
                    category.find_all('a', class_=""))
            else:
                animals[category_char] = list(
                    this.get('title') for this in
                    category.find_all('a', class_=""))
        url = DOMAIN + next_page


if __name__ == '__main__':
    for key, value in counter().items():
        print(key + ': ' + str(len(value)))
