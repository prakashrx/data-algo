def birthday(s, d, m):
    return sum([sum(s[i:i+m]) == d for i in range(0, len(s))])

print(birthday([2,2,1,3,2], 4, 2))