from bs4 import BeautifulSoup
import requests
import csv


def get_html(url: str) -> str:
    ''' Получает html разметку определеннго сайта по url'''
    response = requests.get(url)
    return response.text


def get_soup(html: str):
    '''Получает html разметку и структурирует ее в bs'''
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_last_page(soup: BeautifulSoup) -> int:
    '''Функция которая возврашает послению страницу на сайте!'''
    pages = soup.find('ul', class_ = 'pagination').find_all('a', class_ = 'page-link') 
    last_page = pages[-1].get('data-page')
    return int(last_page)


def get_data(soup: BeautifulSoup) -> list:
    '''Функция парсер получает нужные данные с сайта mashina.kg и возвращает в виде списка'''
    container = soup.find('div', class_ = 'table-view-list')
    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_ = 'name').contents[0].strip()
        try:
            img = car.find('img', class_ = 'lazy-image').get('data-src')
        except:
            img = 'No image!'
        price_div = car.find('div', class_ = 'block price')
        price = price_div.find('p').find('strong').text
        desc1 = car.find('p', class_ = 'year-miles').text.strip()
        desc2 = car.find('p', class_ = 'body-type').text.strip()
        desc3 = car.find('p', class_ = 'volume').text.strip()

        description = f'{desc1} {desc2} {desc3}'
        # ls = ['year-miles', 'body-type', 'volume']

        # desc = ' '.join(car.find('p', class_ = x).text.strip() for x in ls)
        
        data = {
            'name': name, 'desc': description, 'price': price, 'img': img
        }

        result.append(data)
    return result


        # price = car.find('br').contents[0]
        # name2 = car.find('h2', class_ = 'name').text.strip()
        
        # print(name)
        # print(img)
        # print(price)
        # print(desc)
        # print(description)
        # print(pricesom)

def prepare_csv() -> None:
    '''Функция которая подготовливает csv файл!'''
    with open('car.csv', 'w') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'Name': 'Name',
            'Description': 'Description',
            'Price': 'Price',
            'Image URL': 'Image URL'
        })

count = 1        

def write_to_csv(data: dict) -> None:
    '''Записывает все данные в csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
             writer.writerow({
            '№': count, 
            'Name': car['name'],
            'Description': car['desc'],
            'Price': car['price'],
            'Image URL': car['img']
        })
        count += 1

    


def main():
    i = 1

    prepare_csv()
   
    while True:

        url = f'https://www.mashina.kg/search/all/?page= {i}'

        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        data = (get_data(soup))
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 5:
            break
        i += 1

main()





