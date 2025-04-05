# from src.api import HeadHunterAPI
# from src.vacancy import Vacancy
# from src.storage import JSONSaver
# from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
#
#
# def user_interaction():
#     """Функция взаимодействия с пользователем"""
#     print("Программа для поиска вакансий с HeadHunter")
#
#     # Получение данных от пользователя
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()
#     salary_range = input("Введите диапазон зарплат (например: 100000-150000): ")
#
#     # Получение вакансий
#     hh_api = HeadHunterAPI()
#     json_saver = JSONSaver()
#
#     print("\nПолучаем вакансии с HeadHunter...")
#     hh_vacancies = hh_api.get_vacancies(search_query)
#     vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
#     # Сохранение в файл
#     for vacancy in vacancies_list:
#         json_saver.add_vacancy(vacancy)
#
#     # Фильтрация и сортировка
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#
#     # Вывод результатов
#     print("\nРезультаты поиска:")
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()

from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.storage import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слова через пробел: ").split()

    # Получение и сохранение вакансий
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    for vac in vacancies:
        json_saver.add_vacancy(vac)

    # Фильтрация и вывод
    filtered = filter_vacancies(vacancies, filter_words)
    sorted_vac = sort_vacancies(filtered)
    top_vac = get_top_vacancies(sorted_vac, top_n)

    print("\nРезультаты поиска:")
    for i, vac in enumerate(top_vac, 1):
        print(f"{i}. {vac.title}")
        print(f"   Зарплата: {vac.salary_from}-{vac.salary_to}")
        print(f"   Ссылка: {vac.url}\n")


if __name__ == "__main__":
    user_interaction()
