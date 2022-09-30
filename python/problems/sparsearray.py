
def matchingStrings(strings, queries):
    return [sum([1 if q == s else 0 for s in strings]) for q in queries]

print(matchingStrings(['aba', 'baba', 'aba', 'xzxb'],['aba', 'xzxb', 'ab']))