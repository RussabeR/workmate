from statistics import median
from src.reports.base import BaseReport


class MedianCoffeeReport(BaseReport):

    def name(self) -> str:
        return "median_coffee"

    def calculate(self, data: dict) -> list:
        result = [(student, median(values)) for student, values in data.items()]
        return sorted(result, key=lambda x: x[1], reverse=True)
