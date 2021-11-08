
def bubble_sort(ls):
    sorted = False
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            sorted = True
    if sorted:
        bubble_sort(ls)
    return ls


test = [1, 5, 10, 2, 9, 4, 3, 7, 8, 6]
print(bubble_sort(test))
