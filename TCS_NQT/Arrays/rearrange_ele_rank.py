def rank_rearrange(arr):
    sorted_arr = sorted(arr)
    rank_map = {}
    rank = 1
    for num in sorted_arr:
        if num not in rank_map:
            rank_map[num] = rank
            rank += 1
    result = []
    for num in arr:
        result.append(rank_map[num])
    return result
arr = [ 1, 5, 8, 15, 8, 25, 9]
print(rank_rearrange(arr))