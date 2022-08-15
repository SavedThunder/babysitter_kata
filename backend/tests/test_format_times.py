'''
"Leg" in this file is meaning the different 'legs' of time for the sitter

'''

from datetime import datetime, timedelta

from backend.calculate_charge import format_times

TODAY = datetime.today()
TOMORROW = datetime.today() + timedelta(days=1)

def test_format_regular_first_leg():
    formatted = format_times('18:00')
    assert(formatted == TODAY.replace(hour=18, minute=0, second=0, microsecond=0))

def test_format_regular_last_leg():
    formatted = format_times('04:00')
    assert(formatted == TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0))

def test_format_none():
    formatted = format_times(None)
    assert(formatted == None)