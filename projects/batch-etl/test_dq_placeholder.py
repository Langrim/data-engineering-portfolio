"""Lightweight data-quality check (placeholder).
This does not require Spark, just checks the CSV file shape and values.
"""
import pandas as pd
from pathlib import Path

def test_csv_is_non_empty():
    p = Path(__file__).parent / "data" / "input" / "sample_orders.csv"
    df = pd.read_csv(p)
    assert len(df) >= 5, "CSV should have at least 5 rows"

def test_amount_non_negative():
    p = Path(__file__).parent / "data" / "input" / "sample_orders.csv"
    df = pd.read_csv(p)
    assert (df['amount'] >= 0).all(), "Amounts should be non-negative"
