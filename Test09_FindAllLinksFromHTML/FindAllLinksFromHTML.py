__author__ = "call_fold"

import urllib.request
from bs4 import BeautifulSoup

def get_links_from_html(url):
    f= urllib.request.urlopen(url)
    html_content = f.read().decode('utf-8')
    soup = BeautifulSoup(html_content, 'lxml')
    link_list = []
    for link in soup.find_all('a'):
        real_link = link.get('href')
        if 'http' in real_link:
            link_list.append(real_link)
    return link_list

if __name__ == '__main__':
    my_url = 'http://slfweb.com/archives/'
    links = []
    links = get_links_from_html(my_url)
    print(links)