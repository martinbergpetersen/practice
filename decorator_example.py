from functools import partial


def decor(func=None, *, prefix=None):
    if func is None:
        return partial(decor, prefix=prefix)

    def wrapper(*args, **kwargs):
        print(args, kwargs, f'prefix: {prefix}')
        return func(*args, **kwargs)

    return wrapper


@decor(prefix=None)
def cool(name):
    print(name)


print(cool('test'))
