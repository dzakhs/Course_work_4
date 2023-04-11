from url_api_class import UrlApi
import requests


class HeadHunterAPI(UrlApi):
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, demand):
        pass