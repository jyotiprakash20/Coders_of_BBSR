#Insertion at the beginning
# arr= [20, 30, 40]
# ele= 0

# for i in range(len(arr)):
#     print(arr[i], end=' ')
# print()
# arr.insert(0, ele)

# for i in range(len(arr)):
#     print(arr[i], end=' ')

#At given positon
# pos= 2

# arr.insert(pos, ele)
# for i in range(len(arr)):
#     print(arr[i], end=' ')

#At the end
# arr.append(ele)
# for i in range(len(arr)):
#     print(arr[i], end=' ')




#Deletion from the beginning
arr= [35, 67, 58,67, 49,30,20]

# for i in range(len(arr)):
#     print(arr[i], end=' ')
# print()
# del arr[0]
# print(arr)

#From given position
# pos= 3
# del arr[pos]
# for i in range(len(arr)):
#     print(arr[i], end=' ')

#From 1st occurance
# ele= 35
# if ele in arr:
#     arr.remove(ele)
# for i in range(len(arr)):
#     print(arr[i], end =' ')

#2nd occurance
# ele= 67
# k=0
# for i in range(len(arr)):
#     if arr[i] != ele:
#         arr[k]= arr[i]
#         k +=1
# print(k)

#from the end
# for i in range(len(arr)):
#     print(arr[i], end=' ')
# print()
# arr.pop()
# print(arr)

'''Iterating Alternate elements of an array'''

# def print_alternate(arr):
#     res= []

#     for i in range(0, len(arr), 2):
#         res.append(arr[i])
#     return res

# arr= [35, 67, 58,67, 49,30,20]
# result= print_alternate(arr)
# print(result)


'''Leaders in an array'''

# def leaders(arr):
#     res= []
#     n= len(arr)

#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] < arr[j]:
#                 break
#         else:
#             res.append(arr[i])
#     return res
# if __name__ == "__main__":
#     arr= [16, 17, 4, 3, 5, 2]
#     result= leaders(arr)
#     print(result) 

   
'''Check if an Array is Sorted'''

# def is_sorted(arr):
#     n= len(arr)

#     for i in range(1, n):
#         if arr[i] < arr[i-1]:
#             return False
#     return True

# if __name__ == "__main__":
#     arr=[34,23,65,78,123]
#     result= is_sorted(arr)
#     print(result)


'''Remove duplicates from Sorted Array'''

def remove_duplicates(arr):
    seen= set()

    idx=0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx]= arr[i]
            idx +=1
    return idx

if __name__ == "__main__":
    arr= [4,5,7,2,8,4,1,9,7,42,45,77,55,55,44,33,23,11,10,9,8,7,6,5,4,3,2,1]
    result= remove_duplicates(arr)
    for i in range(result):
        print(arr[i], end=' ')
        
    


    



