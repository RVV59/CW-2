from typing import List
from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str], salary_min: int = 0,
                     salary_max: int = float('inf')) -> List[Vacancy]:
    '''фильтрует список вакансий по ключевым словам и диапазону зарплат. Возвращает список вакансий'''
    if not keywords:
        return vacancies
    return [v for v in vacancies if
            (salary_min <= v.salary_from <= salary_max or salary_min <= v.salary_to <= salary_max) and
            any(kw.lower() in (v.description + str(v.requirements)).lower() for kw in keywords)]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    '''Сортирует список вакансий по зарплате от большей к меньшей'''
    return sorted(vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    '''Возвращает первые n вакансий из отсортированного списка'''
    return vacancies[:n]
