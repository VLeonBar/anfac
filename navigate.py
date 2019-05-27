from webscrap import WebScrap as wscrap
from bs4 import BeautifulSoup
import csv


class Nav:

    @staticmethod
    def get_link_from_iframe(html):
        info = html.find("iframe")
        return info['src']

    @staticmethod
    def get_info_from_iframe(html):
        data=[['Fecha','Titulo','Texto']]
        fechas=html.find_all("p", {"class":"fechaNot1"})
        titulos=html.find_all("p", {"class":"titularC"})
        texto=html.find_all("p", {"class":"texto"})
        i=0
        while i<len(fechas):
            data.append([fechas[i].text,titulos[i].text,texto[i].text])
            i+=1
        print(data)

    @staticmethod
    def get_pdf_from_iframe():

        return 0


if __name__ == "__main__":
    wscrap.base_url = "http://www.anfac.com/"
    html = wscrap.get_soup("noticias.action")
    iframe=wscrap.get_soup(Nav.get_link_from_iframe(html))
    Nav.get_info_from_iframe(iframe)
