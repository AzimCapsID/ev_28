from bs4 import BeautifulSoup
import requests
import csv
from multiprocessing import Pool


def adress_html(url: str):
    response = requests.get(url)
    return response.text

def get_soup1(html: str):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_soup(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_last_page(soup: BeautifulSoup):
    pages = soup.find('ul', class_ = 'pagination').find_all('a', class_ = 'page-link') 
    last_page = pages[-1].get('data-page')
    return int(last_page)


def get_data(soup: BeautifulSoup):
    container = soup.find('div', class_ = 'table-view-list')
    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_ = 'name').contents[0].strip()
        try:
            img = car.find('img', class_ = 'lazy-image').get('data-src')
        except:
            img = 'not found'
        price_div = car.find('div', class_ = 'block price')
        price = price_div.find('p').find('strong').text
        priceSom = price_div.find('p').find('br').context
        desc1 = car.find('p', class_ = 'year-miles').text.strip()
        desc2 = car.find('p', class_ = 'body-type').text.strip()
        desc3 = car.find('p', class_ = 'volume').text.strip()

        description = f'{desc1} {desc2} {desc3}'
        
        
        data = {
            'name': name, 'desc': description, 'price': price, 'PriceSom': priceSom, 'img': img
        }
        
        result.append(data)
        
    return result




        
        # name2 = car.find('h2', class_ = 'name').text.strip()
        
        # print(name)
        # print(img)
        # print(price)
        # print(desc)
        # print(description)
# print(priceSom)

def prepare_csv():
    with open('cars.csv', 'w') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'PriceSom', 'Image URL']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'Name': 'Name',
            'Price': 'Price',
            'PriceSom': 'PriceSom',
            'Description': 'Description',
            'Image URL': 'Image URL'
        })

count = 0        

def write_to_csv(data: dict):
    with open('car.csv', 'a') as file:
        fieldnames = ['№', 'Name','Price','PriceSom', 'Image URL', 'Description'  ]
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
            count += 1
            
            writer.writerow({
            '№': count, 
            'Name': car['name'],
            'Price': car['price'],
            'PriceSom': car['PriceSom'],
            'Description': car['desc'],           
            'Image URL': car['img']
        })
        

def main():
    i = 1

    prepare_csv()
   
    while True:

        url = f'https://www.mashina.kg/search/all/?page= {i}'

        html = adress_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        data = (get_data(soup))
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 2:
            break
        i += 1

main()




