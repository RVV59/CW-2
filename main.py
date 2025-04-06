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
    salary_range = input("Введите диапазон зарплат (например, 'от 50000 до 150000'): ")

    try:
        salary_min, salary_max = map(int, salary_range.split('-'))
    except ValueError:
        print("Ошибка ввода диапазона зарплат! Попробуйте снова.")
        exit()

    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    for vac in vacancies:
        json_saver.add_vacancy(vac)

    filtered = filter_vacancies(vacancies, filter_words, salary_min=salary_min, salary_max=salary_max)
    sorted_vac = sort_vacancies(filtered)
    top_vac = get_top_vacancies(sorted_vac, top_n)

    print("\nРезультаты поиска:")
    for i, vac in enumerate(top_vac, 1):
        print(f"{i}. {vac.title}")
        print(f"   Зарплата: {vac.salary_from}-{vac.salary_to}")
        print(f"   Ссылка: {vac.url}\n")


if __name__ == "__main__":
    user_interaction()
