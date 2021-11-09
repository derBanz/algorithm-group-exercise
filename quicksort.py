def partition(lst, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if lst[i] <= lst[low]:
            pivot += 1
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[low] = lst[low], lst[pivot]
    return pivot


def quicksort(lst, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    def _quicksort(lst, low, high):
        if low >= high:
            return
        pivot = partition(lst, low, high)
        _quicksort(lst, low, pivot-1)
        _quicksort(lst, pivot+1, high)
    return _quicksort(lst, low, high)

lst = [7, 1, 3, 15, 11, 10, 2, 21]
print(lst)
quicksort(lst)
print(lst)