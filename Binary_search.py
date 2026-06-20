# def binary_search(arr, x):
#     low=0
#     high= len(arr)-1

#     while low <= high:
#         mid = low +(high -low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid] < x:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# arr1= [23,45,67,45,34,89,90,21,34,32,57,34,23,89,22,100,123321,345,567]
# x= 100
# arr1.sort()
# result= binary_search(arr1,x)

# if result !=-1:
#     print(f'Element {x} is present at index {str(result)}')
# else:
#     print(f'Element {x} is not present in array')


'''Find First and Last Occurrence
 Given a sorted array with duplicate elements, find the first and last index of a given number.
 (Example: arr = [2,4,10,10,10,18,20], x=10 → output: (2,4))'''

# def first_occurence(arr, target):
#     low=0
#     high= len(arr)-1
#     found=-1
#     while low <=high:
#         mid = low + (high-low)//2
#         if arr[mid]== target:
#             found=mid
#             high= mid-1
#         elif arr[mid] < target:
#             low= mid+1
#         else:
#             high= mid -1
#     return found
# def last_occurence(arr, target):
#     low=0
#     high= len(arr)-1
#     found=-1

#     while low <= high:
#         mid = low+(high-low)//2
#         if arr[mid]==target:
#             found= mid
#             low= mid+1
#         elif arr[mid] < target:
#             low= mid+1
#         else:
#             high= mid-1
#     return found

# arr= [2,4,6,2,7,5,2,9,2,4,10,10,10,18,20]
# target= 2
# arr.sort()
# first= first_occurence(arr, target)
# last= last_occurence(arr, target)
# print(f'First Occurrence of {target} is at index {first}')
# print(f'Last Occurrence of {target} is at index {last}')

# if first !=-1 and last !=-1:
#     print(last-first+1)

'''Find Floor and Ceil of an Element
For a given number x, find:

Floor: largest element ≤ x

Ceil: smallest element ≥ x
(Example: arr = [1,2,8,10,10,12,19], x=5 → floor=2, ceil=8)'''

# def find_floor(arr, target):
#     low=0
#     high= len(arr)-1
#     floor=-1
#     while low<=high:
#         mid = low +(high-low)//2
#         if arr[mid]== target:
#             return arr[mid]
#         elif arr[mid] < target:
#             floor= arr[mid]
#             low=mid+1
#         else:
#             high= mid-1
#     return floor

# def find_ceil(arr, target):
#     low=0
#     high= len(arr)-1
#     cell=-1

#     while low <= high:
#         mid = low +(high-low)//2
#         if arr[mid]== target:
#             return arr[mid]
#         elif arr[mid] < target:
#             low= mid+1
#         else:
#             cell= arr[mid]
#             high= mid-1
#     return cell

# arr= [1,2,8,10,10,12,19]
# target= 16
# arr.sort()
# floor= find_floor(arr, target)
# ceil= find_ceil(arr, target)        
# print(f'Floor of {target} is {floor}')
# print(f'Ceil of {target} is {ceil}')


'''Find Insert Position
If the element isn’t found, return the index where it should be inserted to keep the array sorted.
(Example: arr = [1,3,5,6], x=2 → output: 1)'''

# def find_insert_pos(arr, target):
#     low=0
#     high= len(arr)-1

#     while low <= high:
#         mid = low +(high-low)//2

#         if arr[mid]== target:
#             return mid
#         elif arr[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return low
# arr= [1,3,5,6]
# target= 4
# arr.sort()
# result= find_insert_pos(arr, target)
# print(f'Insert position for {target} is {result}')

'''Find Square Root (Without using sqrt())
Given an integer n, find its floor square root using binary search.
(Example: n=10 → output: 3)'''

# def find_sqrt(n):
#     if n==0 or n==1:
#         return n
#     low=1
#     high=n
#     ans= -1

#     while low <= high:
#         mid= low+(high-low)//2
#         if mid*mid==n:
#             return mid
#         elif mid*mid < n:
#             low= mid+1
#             ans= mid
#         else:
#             high= mid-1
#     return ans
# n=int(input('Enter a number: '))
# result= find_sqrt(n)
# print(f'Square root of {n} is {result}')

'''Generating All Subarrays'''

# def sub_arr(arr):
#     n=len(arr)
#     subarray= []

#     for i in range(n):
#         for j in range(i,n):
#             subarray.append(arr[i:j+1])
#     return subarray

# arr=[3, 4, 5]
# result= sub_arr(arr)
# print('Subarrays are:',result)

'''Array Reverse'''

# def reverse_array(arr):
#     left=0
#     right= len(arr)-1

#     while left < right:
#         arr[left], arr[right]= arr[right], arr[left]
#         left+=1
#         right -=1
#     return arr

# arr= [1, 2, 3, 4, 5]
# result= reverse_array(arr)
# print('Reversed array:', result)


'''Rotate an Array - Clockwise or Right'''

# def rotate_array(arr, k):
#     n= len(arr)

#     for i in range(k):
#         last= arr[n-1]
#         for j in range(n-1,0,-1):
#             arr[j]= arr[j-1]
#         arr[0]=last

# arr= [1, 2, 3, 4, 5]
# k=2
# rotate_array(arr, k)
# print('Rotated array:', arr)

'''Move all Zeros to End of Array'''

def move_zeroes(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] !=0:
            arr[i], arr[count]= arr[count], arr[i]
            count +=1
    return arr

arr = [0, 1, 0, 3, 0, 12, 0, 5]
result= move_zeroes(arr)
print('Array after moving zeroes:', result)
