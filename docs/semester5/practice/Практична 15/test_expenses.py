import pytest
from pathlib import Path
from expenses import parse_line, total_by_category, load_expenses


def test_parse_line():
    result = parse_line("2026-09-21;food;85.50;lunch")
    assert result == {
        "date": "2026-09-21",
        "category": "food",
        "amount": 85.50,
        "comment": "lunch"
    }


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_invalid_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


@pytest.mark.parametrize("line, category, amount", [
    ("2026-09-21;food;85.50;lunch", "food", 85.50),
    ("2026-09-21;transport;32.00;bus", "transport", 32.00),
    ("2026-09-22;coffee;65.00;coffee", "coffee", 65.00),
    ("2026-09-23;food;14.50;snack", "food", 14.50),
    ("2026-09-24;books;220.00;book", "books", 220.00),
])
def test_parse_line_parametrize(line, category, amount):
    result = parse_line(line)
    assert result["category"] == category
    assert result["amount"] == amount


def test_total_by_category():
    records = [
        {"category": "food", "amount": 85.50},
        {"category": "food", "amount": 14.50},
        {"category": "transport", "amount": 32.00},
    ]
    assert total_by_category(records) == {
        "food": 100.0,
        "transport": 32.0
    }


def test_load_expenses_tmp_path(tmp_path):
    file_path = tmp_path / "test_expenses.csv"
    file_path.write_text(
        "# Тестові витрати\n\n"
        "2026-09-21;food;85.50;lunch\n"
        "2026-09-22;food;14.50;snack\n",
        encoding="utf-8"
    )

    records = load_expenses(file_path)
    assert len(records) == 2
    assert total_by_category(records) == {"food": 100.0}


def test_real_expenses_file():
    path = Path("data/expenses.csv")
    records = load_expenses(path)

    assert len(records) == 14
    assert total_by_category(records) == {
        "books": 220.0,
        "coffee": 130.0,
        "food": 602.0,
        "internet": 250.0,
        "transport": 96.0
    }
