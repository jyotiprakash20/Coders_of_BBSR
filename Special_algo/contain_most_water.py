def most_water(arr):
    left = 0
    right = len(arr)-1
    maxArea = 0

    while left < right:
        width = right - left
        area = width * min(arr[left], arr[right])

        if area > maxArea:
            maxArea = area
        if arr[left] < arr[right]:
            left += 1
        else:
            right -=1
    return maxArea
height = [1,8,6,2,5,4,8,3,7]
print(most_water(height))