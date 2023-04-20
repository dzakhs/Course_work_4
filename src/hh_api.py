from src.url_api_class import UrlApi
import requests
from src.vacancies import Vacancy


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




       # response = requests.get(url=self.url, params=params)

       # if response.status_code == 200:
        #    data = response.json()
        #    hh_data = data["items"]
        #    vacancies = []
        #    for vacancy in hh_data:
        #        name = vacancy['name'],
        #        url = vacancy['alternate_url'],
        #        description = vacancy['snippet']['requirement'],
        #        experience = vacancy['experience']['name'],
        #        salary_from = vacancy['salary']['from'],
        #        salary_to = vacancy['salary']['to']
        #        post = Vacancies(name, url, description, experience, salary_from, salary_to)
        #        vacancies.append(post)
        #    return vacancies
       # else:
          #  return f"Ошибка: {response.status_code}"


