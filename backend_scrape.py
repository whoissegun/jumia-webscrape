from bs4 import BeautifulSoup
import requests
import pyshorteners

a = 1
def get_data(url,budget,brands:list):
    global a
    
    print(f"Page {a}")
    
    page=requests.get(url).text
    soup = BeautifulSoup(page,'html.parser')
    information = soup.find_all('div',{"class":"info"})
    for info in information:
        price = info.find('div',class_='prc').text
        change = price.replace("₦",'')
        if '-' in change:
            pos = change.find('-')
            new_change = change[0:pos]
            new_change = int(new_change.replace(',','')) 
            change = new_change   
        else:
            change = int(change.replace(',',''))
        
        if change <= budget:
            name= info.find('h3',class_='name').text
            product_link = soup.find('a',{'class':'core'})
            product_link = 'https://www.jumia.com.ng'+product_link['href']
            count = 0
            for brand in brands:
                if brand.lower() not in name.lower():
                    count += 1
            if count == len(brands):
                print(f"{name}. Price {price}. Link: {product_link}")
                
                    
                    
    a += 1

    return soup

def next_page(soup):
    
    if soup.find('a',{'aria-label':f'Page {a}'}):
        link_dict = soup.find('a',{'aria-label':f'Page {a}'})
        link = link_dict['href']    
        link = 'https://www.jumia.com.ng' + link
        return link
    else:
        return

