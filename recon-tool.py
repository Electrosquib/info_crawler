from os import write
import time
from bs4 import BeautifulSoup
import requests
import re

url_input = 'https://xxxxxxxxx.com' # Origin crawler URL

# Values that will be written to a file
urls_list = []
phone_numbers = []
emails = []

# Regular Expressions
email_regex = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
phone_regex = r'\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})'

def write_to_file(url=''):
    with open('output.txt', mode='a') as file:
        f = file.write(str(url)+'\n')
        f = file.write('Phone Numbers: \n')
        for n in phone_numbers:
            f = file.write(str(n)+'\n')
        f = file.write('Emails: \n')
        for em in emails:
            f = file.write(str(em)+'\n')

def get_page(url_req):
    try:
        page = requests.get(url_req)
        return page.text
    except:
        pass
def find_urls(page):
    try:
        soup = BeautifulSoup(page, 'html.parser')
        for links in soup.find_all('a', href=True, text=True):
            urls_list.append(links['href'])
    except:
        pass
def find_emails(text):
    emails.clear()
    try:
        emailz = re.findall(email_regex, text)
        for i in emailz:
            print(i)
            emails.append(i)
    except:
        pass

def find_phone_nums(text):
    phone_numbers.clear()
    try:
        n = re.findall(phone_regex, text)
        print(n)
        for i in n:
            num_string = ''
            for j in i:
                num_string += j
            print(num_string)
            phone_numbers.append(num_string)
    except:
        pass
def crawler(nip=''):
    pager = get_page(nip)
    find_urls(pager)
    find_phone_nums(pager)
    find_emails(pager)
    write_to_file(nip)

print(f'{len(urls_list)} URLs found on origin page')
crawler(url_input)
for count, i in enumerate(urls_list):
    crawler(nip=i)
    print(f'{100*(int(count)/len(urls_list))}% Completed.')
