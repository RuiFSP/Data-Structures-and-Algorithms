from time import time


def timer_func(func):
    def wrapper_func(*arg, **kwargs):
        t1 = time()
        result = func(*arg, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrapper_func


@timer_func
def print_items(a, b):
    for i in range(a):
        print(a)
    for j in range(b):
        print(b)


@timer_func
def print_items_diff_value_args(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


@timer_func
def print_items_same_value_args(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


@timer_func
def print_items_one_arg(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


if __name__ == "__main__":
    print_items_diff_value_args(100, 200)
    print_items_same_value_args(100, 100)
    print_items_one_arg(100)
