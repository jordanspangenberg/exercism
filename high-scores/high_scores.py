import heapq
def latest(scores: [int]) -> int:
    return scores[-1]


def personal_best(scores: [int]) -> int:
    return max(scores)


def personal_top_three(scores: [int]) -> [int]:
    heapq.heapify(scores)
    return heapq.nlargest(3, scores, key=None)
