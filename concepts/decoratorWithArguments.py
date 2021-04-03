import functools

def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator

@repeat(num_times=4)
def greet(name):
    print(f"hello {name}")

greet("Sumit")