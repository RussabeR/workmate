_______________ Запуск __________________

Используем uv для зависимостей

внутри корневой папки:
- uv -sync
далее переходим внутрь виртуального окружения

- python main.py --files math.csv physics.csv programming.csv --report median_coffee

аналогично можно запустить используя uv:

- python main.py --files math.csv physics.csv programming.csv --report median_coffee


___________ Пример вывода _____________
<img width="970" height="656" alt="{D24EAEE9-F61B-4BC8-B84D-0E91A75EF8E6}" src="https://github.com/user-attachments/assets/a713645f-58b2-45dc-b2aa-f8792f475b7c" />
можно задавать разное колличество файлов

<img width="810" height="671" alt="{6281B312-7EA1-470C-95D7-4DBF36A5DA93}" src="https://github.com/user-attachments/assets/7e9d783a-ba57-41e1-93e5-a05e67c1f938" />


_____________ Архитектура ____________

src/services — работа с файлами и агрегация данных

src/reports — отчёты (расчёт бизнес-логики)

src/app.py — оркестрация (связывает всё вместе)

_____________ Добавление нового отчёта ___________

Создать класс, унаследованный от BaseReport

В обязательном порядке реализовать name() и calculate()

Класс автоматически зарегистрируется

_______________ Тестирование __________________

1. unit-тесты для бизнес-логики

2. интеграционные тесты через CLI

используется pytest

______________ Запуск тестов ______________________

Находясь внутри окружения:

- pytest .

либо при помощи uv вне окружения:

- uv run pytest .


Покрытие:

<img width="1357" height="348" alt="{0A3676FD-BED5-496B-965F-6D92A3E6F532}" src="https://github.com/user-attachments/assets/7ca30c6e-884f-444d-b22d-49244fd2fc96" />



_______ Особенности реализации ___________

Используется только стандартная библиотека (argparse, csv, statistics)

поддержка параллельного чтения файлов

чистое разделение слоёв (services / reports / app)
