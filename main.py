import argparse
import traceback
from src.app import run
from src.exceptions import ReportNotFoundError, FileMissingError

def main():
    parser = argparse.ArgumentParser(description="Отчёт о потреблении кофе")
    parser.add_argument("--files", nargs="+", required=True, help="CSV файлы с данными студентов")
    parser.add_argument("--report", required=True, help="Название отчёта")
    args = parser.parse_args()

    try:
        run(args.files, args.report)
    except FileMissingError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except ReportNotFoundError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except Exception:
        print("Произошла непредвиденная ошибка:")
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()