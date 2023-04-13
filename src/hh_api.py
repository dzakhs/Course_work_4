from url_api_class import UrlApi
import requests


class HeadHunterAPI(UrlApi):
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, search_query):
        hh_api = "https://api.hh.ru/vacancies"
        params = {
            "text" : search_query,
            "page" : 10,
            "per_page" : 100,
            "area" : 113,
            "only_with_salary" : True

        }
        response = requests.get(url=hh_api, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                 self.vacancies.append({'name': vacancy['name'],
                                       'url': vacancy['url'],
                                       'description': vacancy['snippet']['requirement'],
                                       'experience' : vacancy['experience']['name'],
                                       'salary_from': vacancy['salary']['from'],
                                       'salary_to': vacancy['salary']['to']
                                       })
            return self.vacancies
        else:
            return f"Ошибка: {response.status_code}"


