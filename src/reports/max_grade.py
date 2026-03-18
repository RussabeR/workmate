from src.reports.base import BaseReport


class MaxGradeReport(BaseReport):

    def name(self) -> str:
        return "max_grade"

    def calculate(self, data: dict) -> list:
        result = [(student, max(values)) for student, values in data.items()]
        return sorted(result, key=lambda x: x[1], reverse=True)
