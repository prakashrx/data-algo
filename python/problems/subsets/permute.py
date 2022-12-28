def swap(word, i, j):
    if i == j:
        return word
    word = list(word)
    word[i],word[j] = word[j],word[i]
    return "".join(word)


def permute_word_rec(word, index, result):
    if index == len(word) - 1:
        result.append(word)
        return 
        
    for i in range(index, len(word)):
        swaped_word = swap(word, index, i)
        permute_word_rec(swaped_word, index + 1, result)

def permute_word(word):
    result = []
    permute_word_rec(word, 0, result)
    return result

print(permute_word("BAD"))