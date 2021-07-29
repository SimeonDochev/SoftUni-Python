import os


class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        if not os.path.exists("./results.txt"):
            with open("results.txt", 'w') as file:
                pass
        with open("results.txt", 'a') as file:
            file.writelines(f"Function {self.function.__name__} was add called. Result: {self.function(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
