from collections import Counter

def min_window(s, t):
    ret = None
    tfreq = dict(Counter(t))
    sfreq = {}
    matched = set()
    left = 0
    for right in range(len(s)):
        c = s[right]
        sfreq[c] = sfreq.get(c, 0) + 1

        if sfreq[c] >= tfreq.get(c, 99999):
            matched.add(c)
        
        while len(matched) == len(tfreq):
            if ret == None or (right - left + 1) <= len(ret):
                ret = s[left:right+1]
            
            c = s[left]
            sfreq[c] -= 1
            if c in tfreq and sfreq[c] < tfreq[c]:
                matched.remove(c)
            left += 1
    return ret


print(min_window("ABAACBBA", "ABC"))
# args = [["ABCD" , "ABC"],
#     ["XYZYX" , "XYZ"],
#     ["ABXYZJKLSNFC" , "ABC"]]

# for a in args:
#     print(min_window(*a))