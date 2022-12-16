
def squared_sum(n):
    s = 0
    while n > 0:
        d =  n % 10
        n = int(n/10)
        s += d**2
    return s


def is_happy_number(n):
    slow = n
    fast = squared_sum(n)

    while fast != slow and fast != 1:
        slow = squared_sum(slow)
        fast = squared_sum(squared_sum(fast))

    return True if fast == 1 else False



print(is_happy_number(23))
print(is_happy_number(2))