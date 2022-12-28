def letter_combinations_rec(char, arr, index, results):
    if index == len(arr):
        results.append(char)
        return

    for i in arr[index]:
        letter_combinations_rec(char + i, arr, index + 1, results)
    

def letter_combinations(digits):
    results = []
    dict = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    arr = [ dict[int(c)] for c in digits ]
    letter_combinations_rec('', arr, 0, results)
    return results

print(letter_combinations("234"))