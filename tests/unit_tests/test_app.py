# tests/unit_tests/app/test_app.py
import pytest
from unittest.mock import MagicMock
from pathlib import Path

from src.app import (
    run,
    normalize_report_name,
    ReportNotFoundError,
    FileMissingError,
)


def test_normalize_report_name():
    assert normalize_report_name("median_coffee") == "median_coffee"
    assert normalize_report_name("MAX_GRADE") == "max_grade"


# -----------------------------
# Юнит-тест run() — проверка поведения зависимостей
# -----------------------------
def test_run_calls_dependencies(monkeypatch):
    # --- Мокаем агрегатор ---
    fake_aggregate = MagicMock(
        return_value={
            "Иванов Сергей": [100, 150],
            "Петров Алексей": [200],
        }
    )
    monkeypatch.setattr("src.app.aggregate_files", fake_aggregate)

    # --- Мокаем класс отчёта и его инстанс ---
    fake_report_instance = MagicMock()
    fake_report_instance.calculate.return_value = "fake_result"
    fake_report_class = MagicMock(return_value=fake_report_instance)
    monkeypatch.setattr(
        "src.app.BaseReport.registry", {"median_coffee": fake_report_class}
    )

    # --- Мокаем проверку файлов, чтобы не падало на FileMissingError ---
    monkeypatch.setattr(Path, "is_file", lambda self: True)

    # --- Вызов тестируемой функции ---
    result = run(["file1.csv", "file2.csv"], "median_coffee")

    # --- Проверяем поведение ---
    fake_aggregate.assert_called_once_with(["file1.csv", "file2.csv"])
    fake_report_class.assert_called_once()  # конструктор вызван
    fake_report_instance.calculate.assert_called_once_with(
        {
            "Иванов Сергей": [100, 150],
            "Петров Алексей": [200],
        }
    )

    # --- Проверяем результат ---
    assert result == "fake_result"


def test_run_unknown_report_raises(monkeypatch):
    # aggregate_files возвращает пустой словарь
    monkeypatch.setattr("src.app.aggregate_files", lambda files: {})
    monkeypatch.setattr("src.app.BaseReport.registry", {"median_coffee": MagicMock()})
    monkeypatch.setattr(Path, "is_file", lambda self: True)

    with pytest.raises(ReportNotFoundError) as exc:
        run(["file1.csv"], "unknown_report")

    assert "Неизвестный отчёт" in str(exc.value)


def test_run_file_missing_raises(monkeypatch):
    # aggregate_files мокаем, но файл отсутствует
    monkeypatch.setattr("src.app.aggregate_files", lambda files: {})
    monkeypatch.setattr("src.app.BaseReport.registry", {"median_coffee": MagicMock()})
    monkeypatch.setattr(Path, "is_file", lambda self: False)

    with pytest.raises(FileMissingError) as exc:
        run(["file1.csv"], "median_coffee")

    assert "Файл не найден" in str(exc.value)
