arr = []


def rec_fib(n):
    if n == 0:
        arr.append(n)
        print(n)
        n += 1
        return rec_fib(n)

    elif n == 1 and len(arr) == 1:
        arr.append(n)
        print(n)
        return rec_fib(n)

    elif len(arr) > 1 and n < 100000:
        print(arr[len(arr) - 1] + arr[len(arr) - 2])
        arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
        return rec_fib(arr[len(arr) - 1] + arr[len(arr) - 2])


rec_fib(0)
