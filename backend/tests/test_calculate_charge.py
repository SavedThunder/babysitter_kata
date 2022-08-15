from backend.calculate_charge import calculate_nightly_charge
from datetime import datetime, timedelta


TODAY = datetime.today()
TOMORROW = datetime.today() + timedelta(days=1)

def test_outside_hours_early():
    start_time = TODAY.replace(hour=16, minute=0, second=0, microsecond=0)
    end_time = TODAY.replace(hour=19, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time)
    assert(charge == 24)

def test_outside_hours_late():
    start_time = TODAY.replace(hour=22, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=5, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time)
    assert(charge == 88)

def test_inside_hours_regular():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0)
    bed_time = TODAY.replace(hour=20, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time, bed_time)
    assert(charge == 132)

def test_calcaulte_charge_5_2_4():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0)
    bed_time = TODAY.replace(hour=22, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time, bed_time)
    assert(charge == 140)

def test_calculate_charge_2_3_4():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0)
    bed_time = TODAY.replace(hour=19, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time, bed_time)
    assert(charge == 128)

def test_start_end_no_bed_before_midnight():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TODAY.replace(hour=22, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time)
    assert(charge == 60)

def test_start_end_no_bed_after_midnight():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=2, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time)
    assert(charge == 116)

def test_bed_after_midnght():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0)
    bed_time = TOMORROW.replace(hour=1, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time, bed_time)
    assert(charge == 148)

def test_no_bedtime():
    start_time = TODAY.replace(hour=17, minute=0, second=0, microsecond=0)
    end_time = TOMORROW.replace(hour=4, minute=0, second=0, microsecond=0)

    charge = calculate_nightly_charge(start_time, end_time)
    assert(charge == 148)
