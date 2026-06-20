'''Max Distance Between Two Occurrences'''

def max_dist(arr):

    mp={}
    res=0

    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]]=i
        
        else:
            res = max(res, i - mp[arr[i]])
    return res
arr=[2,3,4,2,5,6,2,6,7,8,5,4,2,8,9,1]
result=max_dist(arr)
print(result)