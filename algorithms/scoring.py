def calculate_score(
    distance,
    urgency,
    days_since_donation
):

    # Blood compatibility
    compatibility_score = 30

    # Urgency score
    urgency_scores = {
        "Critical": 25,
        "High": 18,
        "Medium": 10
    }

    urgency_score = urgency_scores.get(urgency, 0)

    # Distance score
    distance_score = max(
        0,
        25 * (1 - distance / 50)
    )

    # Donation recency score
    if days_since_donation is None:
        recency_score = 5
    else:
        recency_score = min(
            10,
            days_since_donation / 90 * 10
        )

    # Availability score
    availability_score = 10

    total = (
        compatibility_score
        + urgency_score
        + distance_score
        + recency_score
        + availability_score
    )

    return round(min(100, total), 2)