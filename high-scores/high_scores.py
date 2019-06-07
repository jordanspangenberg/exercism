import heapq
def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    heapq.heapify(scores)
    return heapq.nlargest(3, scores, key=None)
