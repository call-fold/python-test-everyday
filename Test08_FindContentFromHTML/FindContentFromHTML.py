__author__ = "call_fold"

import urllib.request
from bs4 import BeautifulSoup


def get_content_from_html(url):
    f = urllib.request.urlopen(url)
    html_content = f.read().decode('utf-8')
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text()
    print(text)
    return text
    # r = re.compile(r'<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    # return r.findall(html_content)


if __name__ == '__main__':
    url = 'http://slfweb.com/11/'
    content = get_content_from_html(url)
    with open('slfweb.com_11.txt', 'w') as file:
        for line in content:
            file.write(line)
