from src.saver_class import Saver
import json
from src.vacancies import Vacancy
from src.hh_api import HeadHunterAPI
from src.sjob_api import SuperJobApi


class JSONSaver(Saver):
    def __init__(self, keyword):
        self.__filename = f'{keyword.title()}_vacancies.json'

    @property
    def filename(self):
        return self.__filename

    def add_data(self, data, platform):
        id = 0
        vacancies = []
        vacancies_dict = {}
        if isinstance(platform, HeadHunterAPI):
            for row in data:
                if row['salary']['currency'] == 'RUR':
                    vacancies.append(Vacancy(row['name'], row['alternate_url'], row['snippet']['requirement'], row['experience']['name'],
                            row['salary']['from'], row['salary']['to']))
            for vacancy in vacancies:
                vacancies_dict[f'{id + 1}'] = {'name' : vacancy.name,
                                               'url' : vacancy.url,
                                               'description' : vacancy.description,
                                               'experience' : vacancy.experience,
                                               'salary_from' : vacancy.salary_from,
                                            'salary_to' : vacancy.salary_to
                                               }
                id += 1
        if isinstance(platform, SuperJobApi):
            for row in data:
                if row['payment_from'] == 0 and row['payment_to'] == 0:
                    continue
                else:
                    vacancies.append(
                        Vacancy(row['profession'], row['link'], row['candidat'], row['experience']['title'],
                                row['payment_from'], row['payment_to']))

            for vacancy in vacancies:
                vacancies_dict[f'{id + 1}'] = {'name': vacancy.name,
                                               'url': vacancy.url,
                                               'description': vacancy.description,
                                               'experience': vacancy.experience,
                                               'salary_from': vacancy.salary_from,
                                               'salary_to': vacancy.salary_to
                                               }
                id += 1


        with open(self.__filename, 'w', encoding='utf-8') as outfile:
             json.dump(vacancies_dict,outfile, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)



    def get_data(self):
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data




    def delete_data(self):

        pass

