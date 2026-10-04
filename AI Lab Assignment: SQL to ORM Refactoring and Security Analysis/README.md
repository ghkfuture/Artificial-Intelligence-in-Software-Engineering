# AI Lab Assignment: SQL to ORM Refactoring and Security Analysis

## Overview
This task demonstrates refactoring a procedural database script written in raw SQL (`mysql.connector`) into a robust object-oriented solution using **SQLAlchemy 2.0 ORM**.

## Files in this Folder
- `legacy_procedural.py`: The initial procedural script with raw SQL query execution.
- `refactored_orm.py`: Refactored Python implementation utilizing SQLAlchemy declarative models, session handling, and typed CRUD operations.
- `README.md`: Task overview and file documentation.

## Benefits Implemented
1. **Security & Injection Prevention**: SQL injection mitigation via AST parameterized query expression compilation.
2. **Declarative Mapping**: Strong type definitions and model bindings via `DeclarativeBase` and `mapped_column`.
3. **Session Context Management**: Automatic commit, rollback, and cursor cleanup using context managers (`SessionLocal`).
