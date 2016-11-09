__author__ = "call_fold"

import Common.CrawlerToHTML

if __name__ == '__main__':
    my_url = 'http://slfweb.com/archives/'
    links = []
    links = Common.CrawlerToHTML.get_links_from_html(my_url, 'http')
    print(links)
