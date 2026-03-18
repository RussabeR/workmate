import csv
from src.services.aggregator import read_file


def test_read_file(tmp_path):
    file = tmp_path / "data.csv"
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "student",
                "date",
                "coffee_spent",
                "sleep_hours",
                "study_hours",
                "mood",
                "exam",
            ]
        )
        writer.writerow(
            ["Иванов Сергей", "2024-06-01", "100", "7", "5", "отлично", "Математика"]
        )
        writer.writerow(
            ["Тестова Анна", "2024-06-02", "150", "6", "6", "устал", "Физика"]
        )

    result = read_file(str(file))

    assert result == [("Иванов Сергей", 100), ("Тестова Анна", 150)]
