# Quick Sort

## IDEA

1. During Partition, we choose a pivot element and partition the array around the pivot. (`Pick an element, put every element smaller than the pivot to the left, and every element larger than the pivot to the right. Keep doing this until the array is sorted`)

- Why `if left < right`?
    ```python
    pivot = partition(array, left, right)
    quickSort(array, left, pivot - 1) # sorted, just skip
    quickSort(array, pivot + 1, right) # sorted, just skip
    ```
    - Left hand side 
        - if pivot == left -> nothing smaller than pivot -> left hand side is sorted
        - if pivot == left + 1 -> one element is smaller than pivot -> left hand side is sorted
    - Right hand side
        - if pivot == right -> nothing larger than pivot -> right hand side is sorted
        - if pivot == right - 1 -> one element is larger than pivot -> right hand side is sorted

> Both left hand side and right hand side, if left >= right -> sorted