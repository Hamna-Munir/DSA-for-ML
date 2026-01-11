# Two Pointers Example
# Check if a sorted array contains two numbers with a given sum

def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


numbers = [1, 2, 4, 7, 11, 15]
print(has_pair_with_sum(numbers, 9))
print(has_pair_with_sum(numbers, 20))

# Output:
# True
# False
