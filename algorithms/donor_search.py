def group_donors_by_blood_group(donors):

    donor_map = {}

    for donor in donors:

        bg = donor["blood_group"]

        if bg not in donor_map:
            donor_map[bg] = []

        donor_map[bg].append(donor)

    return donor_map


def binary_search_distance(distances, target):

    left = 0
    right = len(distances) - 1

    while left <= right:

        mid = (left + right) // 2

        if distances[mid] == target:
            return mid

        elif distances[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1