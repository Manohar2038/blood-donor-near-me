import heapq


def get_top_donors(donors, k):

    if k <= 0:
        return []

    heap = []

    for donor in donors:

        item = (
            donor["score"],
            donor["user_id"],
            donor
        )

        if len(heap) < k:
            heapq.heappush(heap, item)

        elif item[:2] > heap[0][:2]:
            heapq.heapreplace(heap, item)

    result = []

    while heap:
        result.append(heapq.heappop(heap)[2])

    return result[::-1]