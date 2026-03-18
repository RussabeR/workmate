from collections import defaultdict
from unittest.mock import patch
from src.services.aggregator import aggregate_files


def test_aggregate_files_unit():
    fake_file_data = [
        [("Иванов Сергей", 100), ("Петров Алексей", 200)],
        [("Иванов Сергей", 150), ("Смирнова Анна", 300)],
    ]

    with patch("src.services.aggregator.read_file", side_effect=fake_file_data):
        result = aggregate_files(["file1.csv", "file2.csv"], use_multiprocessing=False)

    assert isinstance(result, defaultdict)
    assert result["Иванов Сергей"] == [100, 150]
    assert result["Петров Алексей"] == [200]
    assert result["Смирнова Анна"] == [300]
