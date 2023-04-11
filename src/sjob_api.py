from url_api_class import UrlApi
import requests
import os


class SuperJobApi(UrlApi):

    def __init__(self):
        self.vacancies = []


    def get_vacancies(self, demand):
        pass