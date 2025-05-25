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

def test_format_date_result_edge_cases():
    # Test with a leap year date
    date = datetime.date(2024, 2, 29)
    result = format_date_result(date)
    assert result["Standard"] == "February 29, 2024"
    assert result["ISO"] == "2024-02-29"
    assert result["Day of Week"] == "Thursday"

    # Test with the minimum date
    date = datetime.date.min
    result = format_date_result(date)
    assert result["ISO"] == "0001-01-01"

    # Test with the maximum date
    date = datetime.date.max
    result = format_date_result(date)
    assert result["ISO"] == "9999-12-31"

def test_calculate_age_breakdown_edge_cases():
    # Test with 0 days
    result = calculate_age_breakdown(0)
    assert result == "0 days"

    # Test with a very large number of days
    result = calculate_age_breakdown(100000)
    assert "273 years" in result

def test_get_holidays_between_edge_cases():
    # Test with a range that includes only one holiday
    start_date = datetime.date(2023, 7, 1)
    end_date = datetime.date(2023, 7, 4)
    holidays = get_holidays_between(start_date, end_date)
    assert len(holidays) == 1
    assert holidays[0][1] == "Independence Day"

    # Test with a range that starts and ends on a holiday
    start_date = datetime.date(2025, 1, 1)  # New Year's Day
    end_date = datetime.date(2025, 12, 25)  # Christmas Day
    holidays = get_holidays_between(start_date, end_date)
    assert any(holiday[1] == "New Year's Day" for holiday in holidays)
    assert any(holiday[1] == "Christmas Day" for holiday in holidays)
