# Searching & Sorting Notes

## Searching

Searching means finding an element in a collection of data.

### 1. Linear Search

* Checks elements one by one.
* Works on sorted and unsorted lists.
* Easy to implement.

### Code

```python
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))
```

Output:

```text
2
```

### Time Complexity

* Best Case: O(1)
* Average Case: O(n)
* Worst Case: O(n)


## 2. Binary Search

* Works only on sorted lists.
* Divides the search space in half each time.
* Faster than linear search.

### Code

```python
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50]

print(binary_search(numbers, 40))
```

Output:

```text
3
```

### Time Complexity

* Best Case: O(1)
* Average Case: O(log n)
* Worst Case: O(log n)

# Sorting

Sorting means arranging data in ascending or descending order.

Example:

```text
[5, 2, 8, 1]

↓

[1, 2, 5, 8]
```

---

## Bubble Sort

* Compares adjacent elements.
* Swaps if they are in the wrong order.
* Repeats until sorted.

### Code

```python
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [5, 1, 4, 2, 8]

print(bubble_sort(numbers))
```

Output:

```text
[1, 2, 4, 5, 8]
```

### Time Complexity

* Best Case: O(n)
* Average Case: O(n²)
* Worst Case: O(n²)

# Key Takeaways

* Linear Search checks one by one.
* Binary Search works only on sorted lists.
* Bubble Sort repeatedly swaps adjacent elements.
* Binary Search is faster than Linear Search for large datasets.
* Bubble Sort is simple but inefficient for large data.
