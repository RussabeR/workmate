import sys

import pytest
from main import main


def test_cli_runs_successfully(tmp_csv_files, sample_report_registry, capsys):
    sys.argv = ["main.py", "--files"] + [str(f) for f in tmp_csv_files] + ["--report", "median_coffee"]

    main()

    captured = capsys.readouterr()
    output = captured.out


    assert "Иванов Сергей" in output
    assert "Тестова Анна" in output
    assert "Студентов Петр" in output


    assert "250" in output
    assert "400" in output
    assert "600" in output


def test_cli_unknown_report_raises(tmp_csv_files, capsys):
    sys.argv = ["main.py", "--files", str(tmp_csv_files[0]), "--report", "unknown_report"]

    with pytest.raises(SystemExit) as exc:
        main()

    captured = capsys.readouterr()
    assert "Неизвестный отчёт" in captured.out
    assert exc.value.code == 1


def test_cli_file_missing_raises(tmp_path, capsys):
    missing_file = tmp_path / "missing.csv"
    sys.argv = ["main.py", "--files", str(missing_file), "--report", "median_coffee"]

    with pytest.raises(SystemExit) as exc:
        main()

    captured = capsys.readouterr()
    assert "Файл не найден" in captured.out
    assert exc.value.code == 1