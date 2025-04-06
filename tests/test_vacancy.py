from src.vacancy import Vacancy

def test_vacancy_creation():
    vac = Vacancy(
        title="Python Dev",
        url="https://hh.ru/vacancy/123",
        salary_from=100000,
        salary_to=150000,
        description="Test description",
        requirements="Test requirements"
    )
    assert vac.title == "Python Dev"
    assert vac.salary_from == 100000

def test_salary_comparison():
    vac1 = Vacancy("A", "#", 100000, 0, "", "")
    vac2 = Vacancy("B", "#", 150000, 0, "", "")
    assert vac1 < vac2
