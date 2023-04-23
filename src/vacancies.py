import json

class Vacancy:
    __slots__ = ('name', 'url','description','salary_from', 'salary_to', 'experience')
    def __init__(self, name, url, description, experience, salary_from, salary_to):
        self.name = name
        self.url = url
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience



    def __str__(self):
        return f"Название вакансии: {self.name}\n"\
               f"Ссылка: {self.url}\n"\
               f"Описание: {self.description}\n"\
               f" Опыт: {self.experience}\n"\
               f"Зарплата: От: {self.salary_from}, до: {self.salary_to}"

    def __repr__(self):
        return f"Название вакансии: {self.name}\n"\
               f"Ссылка: {self.url}\n"\
               f"Описание: {self.description}\n"\
               f" Опыт: {self.experience}\n"\
               f"Зарплата: От: {self.salary_from}, до: {self.salary_to}"



    def __gt__(self, other):
        if not other.salary_from:
            return True
        if not self.salary_from:
            return False
        return int(self.salary_from) >= int(other.salary_from)


class VacancyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vacancy):
            return obj.__slots__
        return json.JSONEncoder.default(self, obj)


