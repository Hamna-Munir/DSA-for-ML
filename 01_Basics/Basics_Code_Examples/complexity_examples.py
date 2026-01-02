# Complexity Analysis Examples

# O(1) - Constant Time
def get_first_element(arr):
    return arr[0]

# O(n) - Linear Time
def print_elements(arr):
    for element in arr:
        print(element)

# O(n^2) - Quadratic Time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

data = [1, 2, 3, 4]

print(get_first_element(data))
print_elements(data)
print_pairs(data)

# Output:
# 1
# 1
# 2
# 3
# 4
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4
