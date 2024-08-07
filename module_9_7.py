def is_prime(func):
    def wrapper(*args, **kwargs):
        j = func(*args)
        k = 0
        for i in range(2, j // 2 + 1):
            if (j % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")

        return j

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 4, 6)
print(result)
