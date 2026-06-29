def sec_smallest_largest(arr):
    smallest = float('inf')
    second_smallest = float('inf')

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:

        # Second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif smallest < num < second_smallest:
            second_smallest = num

        # Second largest
        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num > second_largest:
            second_largest = num

    return second_smallest, second_largest


arr = [1, 2, 4, 7, 7, 5]
print(sec_smallest_largest(arr))