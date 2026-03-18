from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from src.services.file_reader import read_file


def aggregate_files(file_paths: list[str], use_multiprocessing=True) -> dict[str, list[int]]:
    student_data = defaultdict(list)

    if use_multiprocessing:
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            results = executor.map(read_file, file_paths)
            for file_data in results:
                for student, value in file_data:
                    student_data[student].append(value)
    else:
        for file_path in file_paths:
            for student, value in read_file(file_path):
                student_data[student].append(value)

    return student_data
