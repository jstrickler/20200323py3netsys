#!/usr/bin/env python
import bs4

with open('bookmarks_3_3_17.html') as bookmarks_in:
    soup = bs4.BeautifulSoup(bookmarks_in.read(), 'lxml')

python_header = soup.find('h3', string="Python").parent.next_sibling

for sub_header in python_header.find_all('h3'):
    print(sub_header.string)
    sub_list = sub_header.parent.next_sibling
    if sub_list:
        for link in sub_list.find_all('a'):
            print('\t' + link.string)
            print('\t\t==>', link.get('href'))
