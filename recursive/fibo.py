def loop(records):
    records_length = [len(record) for record in records]
    return sum(records_length)


rec = [['s', 'e'], ['s'], ['sdasd', 'rere', 'dsadae', 'dsadas']]

print(loop(rec))


def fib(n):
    a = 25 + 30
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
