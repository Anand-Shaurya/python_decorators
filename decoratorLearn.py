import time 


def timeLogger(func):
    def export(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Time taken = {t2-t1}")
    return export

def func1(s, p=0):
    i = 0
    while i < 100000000:
        i += 1
    print(str(i)+s)

timeLogger(func1)("ram",p=1)