def pair_sum(numbers, k):
    if len(numbers) <= 1:
        return None

    out = set()
    for idx, number in enumerate(numbers):
        for target_idx, target in enumerate(numbers):
            if target + number == k and idx != target_idx:
                _min = min(number, target)
                _max = max(number, target)
                out.add((_min, _max))
    return out


def pair_sum_fast(numbers, k):
    if len(numbers) <= 1:
        return None
    out = set()
    seen = set()
    for number in numbers:
        target = k - number
        if target not in seen:
            seen.add(number)
        else:
            _min = min(number, target)
            _max = max(number, target)
            out.add((_min, _max))
    return out


cool = range(1000)
print(pair_sum(cool, 55))
print(pair_sum_fast(cool, 55))
