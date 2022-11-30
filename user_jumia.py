from backend_scrape import *
import re
import pyperclip

while True:
    
    print("Copy the link you want to scrape. JUST COPY DO NOT PASTE")
    question = input("If you have copied the link, press enter > ")
    if question != '':
        continue
    link = pyperclip.paste()
    print(f"This '{link}' is the link you want to scrape")
    pattern = re.compile(r'^https://www\.jumia\.com\.ng/catalog/\?q=.+')
    match = pattern.search(link)
    if match:
        print('Correct link inputted')
        budget = input("What's your budjet(highest price you are willing to pay) ")
        if budget.isdigit():
            budget = int(budget)
            break
        elif budget == '': #handles case where user doesn't input anything for budget
            budget = 10000000000 #make budget very large number because nothing in the catalogue will ever have this price
            break
        
        else:
            print("You did not type an integer")
            continue
    else:
        print('Incorrect link inputted')
        print("Example of correct link: https://www.jumia.com.ng/catalog/?q=phone")

print("Are there any brands you are not interested in")
print("If there are please specify (using a comma to separate the different brands)")
print("If there aren't just press enter")
brands = input('> ').split(',')


if __name__ == '__main__':
    
    while True:
        soups = get_data(link,brands,budget)
        link=next_page(soups)
        if not link:
            break