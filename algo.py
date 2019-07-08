from time import time
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('logging', func.__name__)
        return func(*args, **kwargs)

    return wrapper


def timer(active=True):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            before = time()
            result = func(*args, **kwargs)
            print('time: ', abs(time() - before), func.__name__, active)
            return result

        return inner

    return wrapper


def compare(s1, s2):
    return s1.upper() == s2.upper()


def compare_long(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_iter = iter(s2)
    for _s1 in iter(s1):
        _s2 = s2_iter.next()
        if not _s1.lower() == _s2.lower():
            return False
    return True


def palindrom(s1):
    return s1 == reverse(s1)


def reverse_slow(s1):
    reversed = ''
    for char in s1:
        reversed = char + reversed
    return reversed


def reverse(s1):
    reversed_ = ''
    out_idx = len(s1) - 1
    for _ in range(len(s1)):
        reversed_ += s1[out_idx]
        out_idx -= 1
    return reversed_


def difference_list(list1, list2):
    _tmp = {}
    for number in list1:
        if number in _tmp:
            _tmp[number] += 1
        else:
            _tmp[number] = 1

    for number in list2:
        if number in _tmp:
            _tmp[number] -= 1
        else:
            _tmp[number] = 1

    return [key for (key, value) in _tmp.items() if value > 0]


def slow(list1, list2):
    out = []
    for l1 in list1:
        if l1 not in list2:
            out.append(l1)
    for l2 in list2:
        if l2 not in list1:
            out.append(l2)
    return out


def find_missing_fast(list1, list2):
    _tmp = {value: value for value in list2}
    return [l1 for l1 in list1 if l1 not in _tmp]


def find_missing_item(list1, list2):
    return [l1 for l1 in list1 if l1 not in list2]


def reversing_int(int):
    pass


def pair_sum(numbers, k):
    if len(numbers) < 2:
        return []

    # tracking
    seen = set()
    output = set()

    for number in numbers:
        # create a var
        # containig difference between k and number
        target = k - number
        if target not in seen:
            seen.add(number)
        else:
            _min = min(number, target)
            _max = max(number, target)
            output.add((_min, _max))

    return output


@timer(active=False)
def list_union_fast(list1, list2):
    _list1 = set(list1)
    return list1 + [num for num in list2 if num not in _list1]


@timer(active=True)
def list_union(list1, list2):
    return list1 + [num for num in list2 if num not in list1]


@timer
def count(list1, list2):
    count = {}
    for num in list1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in list2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return count


class myset:
    def __init__(self, list):
        self._list = set(list)

    @timer
    def difference(self, other):
        return self._list - myset(other)._list

    @timer
    def union(self, other):
        return self._list | myset(other)._list

    def __sub__(self, other):
        return self.difference(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return repr(self._list)


def reverse_int(int1):
    reversed_ = ''
    for char in reverse(str(int1)):
        if char == '-':
            continue
        reversed_ += char

    if int1 < 0:
        return int(reversed_) * (-1)
    return int(reversed_)


print(reverse_int(113))
# {1, 2, 3, 4, 5, 6} - set(range(1000000000))
# yeah = myset([1, 2, 3, 4, 5, 10000000000])
# print(yeah | [1, 3, 4, 5, 6, 8, 9])
# print(yeah)
# print(set([1, 2, 3, 4, 5, 6]))
# print(yeah - range(10000000))
# print((1, 23, 4))

# print(count([1, 2, 3, 4], [1, 2, 3, 4, 7, 8, 9]))
list_union_fast(list(range(10000000)), list(range(100000)))
list_union(list(range(10000)), list(range(1000)))

# print(compare('abc', 'abc'))  # True
# print(compare_long('abc', 'abcf'))  # False
# print(compare_long('abc', 'abc'))  # True
# print(reverse('nme'))  # cba
# print(list({1, 2, 4} ^ {4, 5, 6}))
# print(difference_list([1, 2, 4], [4, 5, 6]))
# print({4, 12, 9, 5, 8, 6} - {4, 9, 12, 6})
# print(find_missing_fast([4, 12, 9, 5, 8, 6], [4, 9, 12, 6]))
# print(find_missing_item([4, 12, 9, 5, 8, 6], [4, 9, 12, 6]))
# print(find_missing_item(range(101, 111), range(1, 100)))
# print(find_missing_fast(range(101, 111), range(1, 100)))
# print(pair_sum([4, 2, 6], 5))

print(palindrom('sabbas'))
print(reverse_slow('abc'))
