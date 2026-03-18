from pathlib import Path
from tabulate import tabulate
from src.reports.base import BaseReport
from src.services.aggregator import aggregate_files
from src.exceptions import ReportNotFoundError, FileMissingError

def normalize_report_name(name: str) -> str:
    return name.lower()

def run(files: list[str], report_name: str):
    for file_path in files:
        if not Path(file_path).is_file():
            raise FileMissingError(f"Файл не найден: {file_path}")

    report_name_norm = normalize_report_name(report_name)
    if report_name_norm not in BaseReport.registry:
        available = ", ".join(BaseReport.registry.keys())
        raise ReportNotFoundError(
            f"Неизвестный отчёт: {report_name}. Доступные отчёты: {available}"
        )

    data = aggregate_files(files)


    report_cls = BaseReport.registry[report_name_norm]()
    result = report_cls.calculate(data)

    print(tabulate(result, headers=["Student", report_name_norm], tablefmt="grid"))
    return result