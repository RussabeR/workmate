
from src.reports.median_coffee import MedianCoffeeReport

def test_median_coffee_report():
    data = {
        "Иванов Сергей": [100, 150],
        "Тестова Анна": [200],
        "Студентов Петр": [50, 300, 150]
    }
    report = MedianCoffeeReport()
    result = report.calculate(data)
    result_dict = dict(result)

    assert result_dict["Иванов Сергей"] == 125
    assert result_dict["Тестова Анна"] == 200
    assert result_dict["Студентов Петр"] == 150



def test_median_skips_empty_values():
    report = MedianCoffeeReport()

    data = {
        "Студентов Петр": [],
        "Тестова Анна": [100, 200],
    }

    result = report.calculate(data)

    assert ("Тестова Анна", 150) in result
    assert all(student != "Студентов Петр" for student, _ in result)