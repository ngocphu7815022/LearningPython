def factorial(num):
    if type(num) is str:
        return None
    elif num < 0:
        return None
    elif type(num) is float:
        return None

    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


print(factorial("aas"))
