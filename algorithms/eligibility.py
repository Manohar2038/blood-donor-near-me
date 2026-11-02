from datetime import date


def is_eligible(
    age,
    weight,
    last_donation_date,
    is_available,
    today=None
):

    if today is None:
        today = date.today()

    if age is None or age < 18:
        return False

    if weight is None or weight < 50:
        return False

    if not is_available:
        return False

    if last_donation_date is not None:

        days = (today - last_donation_date).days

        if days < 90:
            return False

    return True