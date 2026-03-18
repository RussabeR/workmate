
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