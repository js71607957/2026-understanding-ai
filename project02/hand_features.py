from collections import Counter


STRAIGHTS = [set(range(start, start + 5)) for start in range(1, 10)]
STRAIGHTS.append({10, 11, 12, 13, 1})


def describe_hand(cards):
    suits, ranks = zip(*cards)
    groups = sorted(Counter(ranks).values(), reverse=True)
    groups += [0] * (4 - len(groups))
    unique_ranks = set(ranks)
    matching_suits = max(Counter(suits).values())
    possible_straights = sum(unique_ranks <= run for run in STRAIGHTS)
    return [
        *groups, matching_suits, possible_straights,
        int(unique_ranks <= STRAIGHTS[-1]),
    ]
