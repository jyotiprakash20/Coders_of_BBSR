def long_prefix(arr):
    if not arr:
        return ''
    prefix = arr[0]

    for i in arr[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == '':
                return ''
    return prefix
arr = ["flower", "flow", "flight"]
print(long_prefix(arr))