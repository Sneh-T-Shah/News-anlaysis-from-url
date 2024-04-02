# import the necessary packages
from goose3 import Goose
import requests
from googletrans import Translator


# making a class for web scraping
class WebScrap:
    def __init__(self,):
        self.goose = Goose()
        self.translator = Translator()
    def get_text(self,url):
        request = requests.get(url)
        if request.status_code == 200:
            g = Goose()
            article = g.extract(url=url)
            if article.meta_lang == "en":
                text = article.cleaned_text
                title = article.title
            else:
                print("Translating the article to English")
                text = self.translator.translate(article.meta_description).text
                title = self.translator.translate(article.title).text
            return text,title
        return ""