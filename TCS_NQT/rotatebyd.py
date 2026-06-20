def rotateArr(arr, d):
        #code here
        n = len(arr)
        
        d %= n
        temp = [0]*n
        
        for i in range(n-d):
            temp[i] = arr[d+i]
        for i in range(d):
            temp[n-d+i] = arr[i]
        for i in range(n):
            arr[i] = temp[i] 
arr = [1, 2, 3, 4, 5, 6]
d = 2

rotateArr(arr, d)

for i in range(len(arr)):
     print(arr[i], end=" ")
  