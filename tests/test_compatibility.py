
from algorithms.compatibility import is_compatible


def test_universal_donor():

    assert is_compatible("O-", "AB+") is True


def test_universal_donor_to_all_groups():

    groups = [
        "O-", "O+", "A-", "A+",
        "B-", "B+", "AB-", "AB+"
    ]

    for group in groups:
        assert is_compatible("O-", group) is True


def test_universal_recipient():

    assert is_compatible("O-", "AB+") is True
    assert is_compatible("A+", "AB+") is True


def test_incompatible_groups():

    assert is_compatible("AB+", "O-") is False


def test_invalid_blood_group():

    assert is_compatible("XYZ", "AB+") is False
