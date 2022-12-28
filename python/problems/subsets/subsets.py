def find_all_subsets(v):
    
    sets = []

    for i in range(2** len(v)):
        s = set()
        for j in range(len(v)):
             if i & (1 << j):
                s.add(v[j])
        sets.append(list(s))

    return sets



print(find_all_subsets([2,5,7]))