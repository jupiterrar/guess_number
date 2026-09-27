# Guess Number — ООП-версия

## Описание
Текстовая игра «Угадай число», переписанная с процедурного кода на ООП.

## Установка
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

## Запуск
python main.py

## Тесты
pytest -v

## Архитектура
- Game — игровой цикл
- Player — состояние игрока
- UI — ввод/вывод

## Диаграмма
См. docs/uml.md