import requests
from bs4 import BeautifulSoup
from time import sleep
import logging


class WebScrap:

    base_url = ''

    @staticmethod
    def get_soup(url, external=False, retry=999):
        try:
            if not external:
                url = WebScrap.base_url + url
                print(url)
            page = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                                              'content-type': 'text/plain',
                                              'referer': WebScrap.base_url})
            return BeautifulSoup(page.text, 'html.parser')
        except:
            if retry:
                logging.warning("Retry connection ({}): {}".format(retry, url))
                sleep(5)
                return WebScrap.get_soup(url, True, retry - 1)
            return None

    @staticmethod
    def take_info_single_url(url):
        return url[url.index('/'):]
