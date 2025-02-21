def my_max(digits):

    if digits is None:
        return None

    if len(digits) == 0:
        return None

    if len(digits) == 1:
        return digits[0]

    max_value = digits[0]
    for num in digits[1:]:
        if num > max_value:
            max_value = num
    return max_value

def is_perfect(digit):
    suma = 1
    k = 2
    while k*k < digit:
        if digit % k == 0:
            suma += k + digit/k
        k += 1
    if k*k == digit:
        suma += k
    return suma == digit