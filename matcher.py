from datetime import date

from algorithms.compatibility import is_compatible
from algorithms.eligibility import is_eligible
from algorithms.location import haversine
from algorithms.scoring import calculate_score
from algorithms.donor_ranking import get_top_donors

from database import get_donors


def find_best_donors(
    needed_bg,
    patient_lat,
    patient_lon,
    urgency,
    top_k=5
):

    donors = get_donors(needed_bg)

    ranked_donors = []

    for donor in donors:

        if not is_compatible(
            donor["blood_group"],
            needed_bg
        ):
            continue

        if not is_eligible(
            donor["age"],
            donor["weight"],
            donor["last_donation_date"],
            donor["is_available"]
        ):
            continue

        if donor["latitude"] is None or donor["longitude"] is None:
            continue

        distance = haversine(
            float(patient_lat),
            float(patient_lon),
            float(donor["latitude"]),
            float(donor["longitude"])
        )

        days = (
            (date.today() - donor["last_donation_date"]).days
            if donor["last_donation_date"]
            else None
        )

        score = calculate_score(
            distance,
            urgency,
            days
        )

        donor["distance"] = round(distance, 2)
        donor["score"] = score

        ranked_donors.append(donor)

    return get_top_donors(ranked_donors, top_k)