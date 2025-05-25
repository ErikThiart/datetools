import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streamlit_app import format_date_result, calculate_age_breakdown, get_holidays_between
import datetime

def test_format_date_result():
    date = datetime.date(2025, 5, 25)
    result = format_date_result(date)
    assert result["Standard"] == "May 25, 2025"
    assert result["ISO"] == "2025-05-25"
    assert result["Day of Week"] == "Sunday"

def test_calculate_age_breakdown():
    days = 400
    result = calculate_age_breakdown(days)
    assert "1 year" in result
    assert "1 month" in result
    assert "5 days" in result

def test_get_holidays_between():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 12, 31)
    holidays = get_holidays_between(start_date, end_date)
    assert len(holidays) > 0
    assert any(holiday[1] == "New Year's Day" for holiday in holidays)
