def min_window(str1, str2):
    
    length = float('inf')
    ret = ""
    j = 0
    for i in range(0, len(str1)):
        if(str1[i] == str2[j]):
            j += 1
        if j == len(str2):
            j -= 1
            for s in range(i, -1, -1):
                if(str1[s] == str2[j]):
                    j -= 1
                if j <  0:
                    j = s
                    break

            if i-j+1 < length:
                length = i-j+1
                ret = str1[j:i+1]
            j = 0

    return ret

# Driver code
def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
            "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
            "beta", "asd", "abcd"]
    str2 = ["bde", "kzed", "werty", "abc",
            "css", "la", "ab", "as", "pp"]

    for i in range(len(str1)):
        ret = min_window(str1[i], str2[i])
        print(i+1, ". \t Input string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\t Output: ", ret)
        print("-"*97)


if __name__ == '__main__':
    main()
    