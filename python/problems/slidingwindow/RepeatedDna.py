
def find_repeated_sequences(s, k):
    output= set()
    
    hashes = set()
    t = {'A':1, 'C':2, 'G':3, 'T': 4}
    
    if len(s) <= k:
        return output

    h = sum([(4**(k-i-1))*t[s[i]]  for i in range(0, k)]) 
    hashes.add(h)
    for i in range(1, len(s) - k + 1):
        h = ((h -  t[s[i-1]]* (4**(k-1)))*4) + t[s[i+k-1]]
        if h in hashes:
            output.add(s[i:i+k])
        else:
            hashes.add(h)

    return output


def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 10, 13, 30, 30, 21]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: '", inputs_string[i], "'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tOutput: ",  find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
