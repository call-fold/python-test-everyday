__author__ = "call_fold"

import Common.CrawlerToHTML

if __name__ == '__main__':
    url = 'http://slfweb.com/11/'
    content = Common.CrawlerToHTML.get_content_from_html(url)
    with open('slfweb.com_11.txt', 'w') as file:
        for line in content:
            file.write(line)
