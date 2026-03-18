from statistics import median
from src.reports.base import BaseReport


class MedianCoffeeReport(BaseReport):

    def name(self) -> str:
        return "median_coffee"

    def calculate(self, data: dict[str, list[int]]) -> list[tuple[str, float]]:
        result = [
            (student, median(values))
            for student, values in data.items()
            if values
        ]

        return sorted(result, key=lambda x: x[1], reverse=True)
