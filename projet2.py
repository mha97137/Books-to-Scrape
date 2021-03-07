from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
URL = "http://books.toscrape.com"

if __name__ == '__main__':
    def liburua(url):
        ''' récupérer les informations de chaque livre '''
        urlss = str(url)
        res = requests.get(urlss)
        soup = BeautifulSoup(res.text, 'html.parser')
        for book in soup:
            upc = soup.find_all('td')[0].text
            title = soup.find_all('li')[3].text
            pricei = soup.find_all('td')[3].text
            pricee = soup.find_all('td')[2].text
            stock = soup.find_all('td')[5].text
            description = soup.find_all('p')[3].text
            category = str(soup.find('ul', {'class': 'breadcrumb'}).select('li')[2].text).replace("\n", '')
            rat = soup.find("p", class_="star-rating")["class"][1]
            image = "http://books.toscrape.com" + soup.img['src'][5:]
            ''' sauvegarde images couverture. Obtenir toutes les images + fichier .csv environ 2h '''
            photo = requests.get(image).content
            garbitu = title.translate({ord(g): "" for g in "!@#$%^&*()[]{\r};:,./<>?\\|`~-=_+\"\'"})
            izenburu = garbitu.replace(" ", "_") + '.jpg'
            with open('P2/COUVERTURE/'+izenburu, 'wb') as img:
                img.write(photo)
        hiztegia = {
            'product_page_url': urlss,
            'universal_ product_code_upc': upc,
            'title': title,
            'price_including_tax': pricei,
            'price_excluding_tax': pricee,
            'number_available': stock,
            'product_description': description,
            'category': category,
            'review_rating': rat,
            'image_url': image
        }
        return hiztegia

    def write_csv(dictionary, category):
        df = pd.DataFrame(dictionary)
        df.to_csv(f"./P2/CSV/" + category + '.csv', encoding='utf-8-sig')

    def kategoria():
        ''' récupération catégories '''
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        kategoriak = soup.find("ul", {"class": "nav nav-list"}).find_all("li")[1:]
        for category in kategoriak:
            url_kategoriak = URL + '/' + category.a['href']
            write_csv(url_ak(url_kategoriak), category.text.strip())

    def url_ak(url):
        ''' parcours différentes pages '''
        dictionary = []
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        one = soup('article')
        for book in one:
            chercher = book.find('a')
            link = chercher['href']
            links = URL + '/catalogue/' + link.replace("../../../", "")
            dictionary.append(liburua(links))
        try:
            next_section = soup.find('section').find('li', {'class': 'next'}).select('a')
            next_page = next_section[0]['href']
            plit = url.rsplit("/", 1)
            next_url = plit[0] + str("/" + next_page)
            dictionary += url_ak(next_url)
        except:
            pass

        return dictionary

    ''' create folders to save data '''
    try:
        os.mkdir('P2')
    except:
        pass

    try:
        os.mkdir('P2/CSV')
    except:
        pass

    try:
        os.mkdir('P2/COUVERTURE')
    except:
        pass
    
    ''' run the code '''
    kategoria()
