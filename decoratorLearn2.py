import time

def decorator1(func):
    def export(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Time taken = {t2-t1}.")
    return export

@decorator1
def func1(s: int):
    while 10 < s:
        s -= 1    

# decorator1(func1)(1000000):

func1(10000000)

