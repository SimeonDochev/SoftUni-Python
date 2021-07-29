def cache(function):
    def wrapper(n):
        result = function(n)

        if n not in wrapper.log:
            wrapper.log[n] = result

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
