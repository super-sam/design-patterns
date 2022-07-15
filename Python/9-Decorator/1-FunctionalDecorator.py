import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000:.2f}ms to execute")
        return result

    return wrapper


def some_op():
    print("Starting op")
    time.sleep(1)
    print("endinf some op")
    return 123


@time_it
def some_other():
    print("Starting op")
    time.sleep(1)
    print("endinf some op")
    return 123


if __name__ == "__main__":
    some_op = time_it(some_op)
    some_op()
    some_other()