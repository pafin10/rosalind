with open('34.txt', 'r') as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))

# GPT help
# TODO: Write an explanation
def countInv(arr):
    if len(arr) == 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = countInv(arr[:mid])
    right, inv_right = countInv(arr[mid:])
    merged, inv_merged = mergeCount(left, right)
    return merged, inv_left + inv_right + inv_merged


def mergeCount(left, right):
    i = j = invCount = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
            # No need to increase count, left is already smaller, i.e. sorted
        else:
            merged.append(right[j])
            j += 1
            invCount += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, invCount


_, out = countInv(a)
print(out)