def sym_pair(arr):
    d = {}
    res = []
    for a,b in arr:
        if (b,a) in d:
            res.append(((a,b),(b,a)))
        else:
            d[(a,b)] = True
    return res
arr = [ (1,2),(2,1),(3,4),(4,5),(5,4)]
print(sym_pair(arr))

#Time complexity = O(n)