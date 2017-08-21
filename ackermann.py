class memoize(dict):
    # via: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@memoize
def ack(m, n):
    if m < 0 or n < 0:
        raise
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
