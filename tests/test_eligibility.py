
from datetime import date, timedelta

from algorithms.eligibility import is_eligible


def test_donor_eligible_after_90_days():

    last_date = date.today() - timedelta(days=90)

    assert is_eligible(
        25, 60, last_date, True
    ) is True


def test_donor_not_eligible_after_60_days():

    last_date = date.today() - timedelta(days=60)

    assert is_eligible(
        25, 60, last_date, True
    ) is False


def test_donor_not_available():

    last_date = date.today() - timedelta(days=120)

    assert is_eligible(
        25, 60, last_date, False
    ) is False


def test_donor_under_18():

    last_date = date.today() - timedelta(days=120)

    assert is_eligible(
        17, 60, last_date, True
    ) is False


def test_donor_below_project_weight_threshold():

    last_date = date.today() - timedelta(days=120)

    assert is_eligible(
        25, 45, last_date, True
    ) is False


def test_donor_without_previous_donation():

    assert is_eligible(
        25, 60, None, True
    ) is True
