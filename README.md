# Student Record & Attendance Management System (Python)

A modular, menu-driven Python application using nested dictionaries and text-file persistence (`students.txt`) to manage student marks, attendance percentages, and merit rankings.

## Features
- **Fast Roll-Number Lookup (`O(1)`)**: Stores student records in nested Python dictionaries keyed by roll number.
- **Complete CRUD & File Persistence**: Add, search, update, and delete student records with automatic saving to `students.txt`.
- **Merit Ranking & Attendance Alerts**: Ranks students from highest to lowest marks and flags students below the 75% attendance threshold.

## Files
- `records.py` — Core dictionary operations, file read/write functions, and sorting logic
- `main.py` — Interactive `while True` menu-driven CLI
- `test_records.py` — Automated unit tests using Python's `unittest` module

## How to Run
1. Clone or download this repository.
2. Run `python main.py` (or open `main.py` in IDLE and press `F5`).
3. Run unit tests using `python -m unittest test_records.py`.
