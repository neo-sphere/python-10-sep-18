import time

def fib(n):
    a,b = 0,1
    while a<=n:
        time.sleep(1)
        print(a)
        a,b = b, a+b

def fib_list(n):
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a,b = b, a+b

    return result

if __name__ == "__main__":
    fib(100)
    r = fib_list(50)
    print(r)

