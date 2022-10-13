import requests
from bs4 import BeautifulSoup


URL = "https://www.olx.bg/ads/q-babolat/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all('div', {'class':"offer-wrapper"})

for element in results:
    brand = element.h3.strong.text.replace(' ','')
    price = element.find('p', class_='price').text.replace(' ','')
    links = element.h3.a['href']

    with open("Babolat.txt", "a+", encoding="utf-8") as file_object:
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        
        file_object.write(f'Brand: {brand.strip()} \n')
        file_object.write(f'Price: {price.strip()} \n')
        file_object.write(f'link: {links} \n')
        
    #Uncomment if you want to print on the screen
    
    print(f'Brand: {brand.strip()}')
    print(f'Price: {price.strip()}')
    print(f'link: {links}')
    print('\n')