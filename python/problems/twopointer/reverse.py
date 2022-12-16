def rev_string(sentence, start, end):
    left = start
    right = end
    while left < right:
        sentence[left],sentence[right] = sentence[right], sentence[left]
        left += 1
        right -= 1

def reverse_words(sentence):
    sentence = list(sentence)
    rev_string(sentence, 0, len(sentence) - 1)

    start = 0
    for end in range(len(sentence)):
        if sentence[end] == ' ':
            rev_string(sentence, start, end - 1)
            start = end + 1
        elif end + 1== len(sentence):
            rev_string(sentence, start, end)
    


    return ''.join(sentence)






   


print(reverse_words("Hello World"))
print(reverse_words("Hello World 123"))
