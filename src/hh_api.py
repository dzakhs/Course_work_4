from src.url_api_class import UrlApi
import requests



class HeadHunterAPI(UrlApi):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        pages = 10
        params = {
            "text" : keyword,
            "per_page" : 100,
            "area" : 113,
            "only_with_salary" : True

        }
        data = []

        for page in range(pages):

            responce = requests.get(self.url, params=params).json()['items']
            data.extend(responce)
        return data







