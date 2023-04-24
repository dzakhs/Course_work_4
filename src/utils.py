from src.hh_api import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.sjob_api import SuperJobApi



def choose_platform():
    """
    Функция запрашивает у пользователя с какого сайте запрашивать вакансии
    :return: экзепляр класса HeadHunter  или SuperJob
    """
    while True:
         user_input = input('Выберите платформу для поиска вакансий: HH для HeadHunter, SJ для SuperJob  ').upper()
         if user_input == "HH":
             hh = HeadHunterAPI()
             return hh

         elif user_input == "SJ":
             sj = SuperJobApi()
             return sj
         else:
             print("Вы ввели неверный запрос. Повторите попытку")
             continue


def search_query(platform):
    """
    Функция запрашивает вакансии с сайта, сортирует по уровню зарабатной платы и создает экземпляр
    класса JsonSaver
    :param platform: экземпляр класса HeadHunter или SuperJob
    :return: отсортированный список и экземпляр класса JSONSaver
    """
    if isinstance(platform, HeadHunterAPI):
        keyword = input("Введите поисковый запрос  ")
        hh_vac = platform.get_vacancies(keyword)
        vac_list = []
        for vacancy in hh_vac:
            if vacancy['salary']['from'] is None:
                vacancy['salary']['from'] = 0
            vac_list.append(vacancy)
        hh_vac_sorted = sort_by_salary_from_hh(vac_list)
        js_saver_hh = JSONSaver(keyword)
        print(f'Найдено {len(hh_vac)} вакансий')
        return hh_vac_sorted,js_saver_hh

    elif isinstance(platform, SuperJobApi):
        keyword = input("Введите поисковый запрос  ")
        sj_vac = platform.get_vacancies(keyword)
        sj_vac_sorted = sort_by_salary_from_sj(sj_vac)
        js_saver_ss = JSONSaver(keyword)
        print(f'Найдено {len(sj_vac)} вакансий')
        return sj_vac_sorted, js_saver_ss



def filter_vacancies(data, platform):
    """
    Функуия выполняет поиск по ключевым словам в отсортированному списку вакансий
    :param data: отсоритированный список вакансий
    :param platform:экзепляр класса HeadHunter или SuperJob
    :return: список вакансий
    """
    value = input("Введите запрос для фильтрации вакансий: ").lower()
    filtered_list = []
    if value == '':
        print("Ключевые значения не введены, доступны все ваканскии")

        return data
    elif isinstance(value,str):

        print(f'Запуск поиска вакансий по искомому запросу {value}')
        if isinstance(platform, HeadHunterAPI):
            for vacancy in data:
                if vacancy['snippet']['requirement'] is not None:
                    if value in vacancy['snippet']['requirement'].lower():
                        filtered_list.append(vacancy)
                    else:
                        continue
                else:
                    continue
        elif isinstance(platform, SuperJobApi):
            for vacancy in data:
                if vacancy['candidat'] is not None:
                     if value in vacancy['candidat'].lower():
                        filtered_list.append(vacancy)
                     else:
                        continue
                else:
                    continue
        if len(filtered_list) > 0:
            print(f'Найдено {len(filtered_list)} вакансий')
            return filtered_list
        else:
            quit('По вашему запросу вакансии не найдены')


def find_salary(data,platform):
    """
    Функуия выполняет поиск по уровню зарплаты в отсортированном списке вакансий
    :param data: отсоритированный список вакансий
    :param platform:экзепляр класса HeadHunter или SuperJob
    :return: список вакансий

    """
    user_input = input('Укажите уровень заработной платы: ')
    if user_input == '':
        return data
    print('Запуск поиска вакансий по указанной зарплате')
    new_data = []
    if isinstance(platform, HeadHunterAPI):
        for vacancy in data:
            if vacancy['salary']['from'] is not None:
                if int(vacancy['salary']['from']) >= int(user_input):
                    new_data.append(vacancy)
    elif isinstance(platform, SuperJobApi):
        for vacancy in data:
            if vacancy['payment_from'] is not None:
                if int(vacancy['payment_from']) >= int(user_input):
                     new_data.append(vacancy)

    if len(new_data) > 0:
        print(f'Найдено {len(new_data)} вакансий')
        return new_data
    else:
        print("По вашему запросу вакансии не найдены")

def sort_by_salary_from_hh(data):
    """
    Функция сортировки вакансий с сайта hh.ru
    :param data: cписок вакансий
    """
    sort_data = sorted(data, key=lambda x: x['salary']['from'], reverse=True)
    return sort_data


def sort_by_salary_from_sj(data):
    """
    Функция сортировки вакансий с сайта superjob.ru
    :param data: cписок вакансий
    """
    sort_data = sorted(data, key=lambda x: x['payment_from'], reverse=True)
    return sort_data

def top_n_vacancies(data):
    """
    Функция выводит заданное пользователем количество вакансий
    :param data: общий список вакансий
    :return: список вакансий определнных пользователем
    """
    while True:
        user_unput = int(input("Введите количество вакансий для вывода данных: "))
        if user_unput <= len(data):
            return data[:user_unput]
            break
        else:
           print("Нет такого количества вакансий. Повторите попытку.")






def main():
    """
    Функция взаимодествия с пользователем
    :return: json файл с выбранными вакансиями
    """
    platform = choose_platform()     # выбор сайта
    vacancies, json_saver_item = search_query(platform)    #загрузка вакансий
    salary_level = find_salary(vacancies, platform)   #поиск вакансий по зарплате
    user_filter = filter_vacancies(salary_level, platform) #поиск вакансий по ключевым словам
    top_n = top_n_vacancies(user_filter) #вывод необходимого количества вакансий
    json_saver_item.add_data(top_n, platform) #запись вакансий в json файл
    json_saver_item.delete_data()


















