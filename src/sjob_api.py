
from src.url_api_class import UrlApi
import requests
import os

# создаем класс для получения данных о вакансиях с сайта superjob.ru
class SuperJobApi(UrlApi):

    def __init__(self):
        self.api_key = os.getenv("SJ_API")
        self.headers = {'X-Api-App-Id': self.api_key,
                        'Content-Type': 'application/json'
                        }
        self.url = "https://api.superjob.ru/2.0/vacancies/"


    def get_vacancies(self, keyword):
        """
        метод для получения данных о вакансиях с сайте
        :param keyword: ключевое слово для поиска
        :return: список со словарями
        """
        params = {'keyword': keyword,
                  'count': 100,
                  'period': 0,
                  'no_agreement': 1
                  }
        data = []
        response = requests.get(self.url, headers=self.headers, params=params).json()['objects']

        data.extend(response)
        return data








