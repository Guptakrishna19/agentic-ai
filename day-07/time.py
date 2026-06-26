import time

numbers = list(range(1000))
target = 999

# Linear Search
start = time.time()
for i in range(len(numbers)):
    if numbers[i] == target:
        break

end = time.time()

print("Linear Search Time:", end - start)


# Binary Search
start = time.time()

low = 0
high = len(numbers) - 1
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

end = time.time()

print("Binary Search Time:", end - start)