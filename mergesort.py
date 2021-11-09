# TODO implement mergesort


def mergesort(list: list, left=1, right=-1) -> list:
    if right == -1:
        right = len(list)
    if right > left:
        middle = int(left + (right - left) / 2)
        # mergesort both halves
        list = mergesort(list, left, middle)
        list = mergesort(list, middle+1, right)
        # merge the halves
        list = merge(list, left-1, middle-1, right-1)
    return list


def merge(list, left, middle, right) -> list:
    n1 = middle - left + 1
    n2 = right - middle
    # Create temp lists
    left_list = []
    right_list = []
    # Copy data to temp lists
    for i in range(n1):
        left_list.append(list[left + i])
    for i in range(n2):
        right_list.append(list[middle + 1 + i])
    # Merge the temp lists back
    # Initial index of first sublist
    i = 0
    # Initial index of second sublist
    j = 0
    # Initial index of merged sublist
    k = left
    while i < n1 and j < n2:
        if left_list[i] <= right_list[j]:
            list[k] = left_list[i]
            i += 1
        else:
            list[k] = right_list[j]
            j += 1
        k += 1
    # Copy the remaining elements of left_list if any
    while i < n1:
        list[k] = left_list[i]
        i += 1
        k += 1
    # Copy the remaining elements of right_list if any
    while j < n2:
        list[k] = right_list[j]
        j += 1
        k += 1
    return list
