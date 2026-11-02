
from algorithms.donor_ranking import get_top_donors


def test_top_three_donors():

    donors = [
        {"user_id": 1, "score": 70},
        {"user_id": 2, "score": 95},
        {"user_id": 3, "score": 80},
        {"user_id": 4, "score": 90},
        {"user_id": 5, "score": 60}
    ]

    result = get_top_donors(donors, 3)

    scores = [d["score"] for d in result]

    assert scores == [95, 90, 80]


def test_empty_donor_list():

    assert get_top_donors([], 5) == []


def test_top_k_larger_than_donors():

    donors = [
        {"user_id": 1, "score": 80},
        {"user_id": 2, "score": 90}
    ]

    result = get_top_donors(donors, 5)

    assert len(result) == 2
