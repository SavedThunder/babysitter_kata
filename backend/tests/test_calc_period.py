from backend.calculate_charge import calculate_period


def test_calculate_period_zero():
    calc = calculate_period(0, 12)

    assert(calc == 0)

def test_calculate_regular():
    calc = calculate_period(4, 12)
    
    assert(calc == 48)

def test_calculate_decimal_delta():
    calc = calculate_period(4.56, 12)

    assert(calc == 48)
