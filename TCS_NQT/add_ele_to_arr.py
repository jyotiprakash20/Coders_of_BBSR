#Adding at beginning
def add_start(arr,n):
    arr.insert(0, n)
    return arr
#At the end
def add_end(arr,n):
    arr.append(n)
    return arr
#At the specific position
def add_pos(arr,pos,n):
    arr.insert(pos,n)
    return arr
arr = [1,2,3,4,5]
print(add_start(arr, 0))
print(add_end(arr,6))
print(add_pos(arr,3,3.5))