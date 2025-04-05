import pytest
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy


# Тестовые данные для вакансий
def create_vacancy(title, url, salary_from, salary_to, description, requirements):
    return Vacancy(title, url, salary_from, salary_to, description, requirements)


# Тесты для filter_vacancies
def test_filter_vacancies_no_keywords():
    vacancies = [
        create_vacancy("Job 1", "url1", 10000, 15000, "Description 1", "Requirements 1"),
        create_vacancy("Job 2", "url2", 20000, 25000, "Description 2", "Requirements 2")
    ]
    keywords = []
    expected_result = vacancies
    actual_result = filter_vacancies(vacancies, keywords)
    assert actual_result == expected_result


def test_filter_vacancies_with_keywords_present():
    vacancies = [
        create_vacancy("Job 1", "url1", 10000, 15000, "Description keyword1", "Requirements keyword2"),
        create_vacancy("Job 2", "url2", 20000, 25000, "Description keyword3", "Requirements keyword4")
    ]
    keywords = ["keyword1", "keyword2"]
    expected_result = [vacancies[0]]
    actual_result = filter_vacancies(vacancies, keywords)
    assert actual_result == expected_result


def test_filter_vacancies_with_keywords_absent():
    vacancies = [
        create_vacancy("Job 1", "url1", 10000, 15000, "Description", "Requirements"),
        create_vacancy("Job 2", "url2", 20000, 25000, "Description", "Requirements")
    ]
    keywords = ["keyword1", "keyword2"]
    expected_result = []
    actual_result = filter_vacancies(vacancies, keywords)
    assert actual_result == expected_result


# Тесты для sort_vacancies
def test_sort_vacancies_unsorted():
    vacancies = [
        create_vacancy("Job 1", "url1", 30000, 35000, "Description", "Requirements"),
        create_vacancy("Job 2", "url2", 10000, 15000, "Description", "Requirements"),
        create_vacancy("Job 3", "url3", 20000, 25000, "Description", "Requirements")
    ]
    expected_result = [
        create_vacancy("Job 1", "url1", 30000, 35000, "Description", "Requirements"),
        create_vacancy("Job 3", "url3", 20000, 25000, "Description", "Requirements"),
        create_vacancy("Job 2", "url2", 10000, 15000, "Description", "Requirements")
    ]
    actual_result = sort_vacancies(vacancies)
    assert actual_result == expected_result


def test_sort_vacancies_empty_list():
    vacancies = []
    expected_result = []
    actual_result = sort_vacancies(vacancies)
    assert actual_result == expected_result


# Тесты для get_top_vacancies
def test_get_top_vacancies_n_less_than_length():
    vacancies = [
        create_vacancy("Job 1", "url1", 10000, 15000, "Description", "Requirements"),
        create_vacancy("Job 2", "url2", 20000, 25000, "Description", "Requirements"),
        create_vacancy("Job 3", "url3", 30000, 35000, "Description", "Requirements")
    ]
    n = 2
    expected_result = vacancies[:n]
    actual_result = get_top_vacancies(vacancies, n)
    assert actual_result == expected_result


def test_get_top_vacancies_n_greater_than_length():
    vacancies = [
        create_vacancy("Job 1", "url1", 10000, 15000, "Description", "Requirements"),
        create_vacancy("Job 2", "url2", 20000, 25000, "Description", "Requirements"),
        create_vacancy("Job 3", "url3", 30000, 35000, "Description", "Requirements")
    ]
    n = 10
    expected_result = vacancies
    actual_result = get_top_vacancies(vacancies, n)
    assert actual_result == expected_result


def test_get_top_vacancies_empty_list():
    vacancies = []
    n = 2
    expected_result = []
    actual_result = get_top_vacancies(vacancies, n)
    assert actual_result == expected_result
