# поиск перебором
def simple_search(lst, target):
    for ind, item in enumerate(lst):
        print(f"Ищу по индексу {ind}")
        if item == target:
            return ind
    return "не найдено"


print("При помощи поиска перебором")
my_numbers = [1, 2, 3, 5, 7, 11, 12]
print(simple_search(my_numbers, 12))
print("------")
print(simple_search(my_numbers, 7))
print("------")
print(simple_search(my_numbers, 6))
print("------")


def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    steps = 0
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if lst[middle] == target:
            print(steps)
            return middle
        elif lst[middle] < target:
            left = middle + 1
        elif lst[middle] > target:
            right = middle - 1

    print(steps)
    return "не найдено"


print("При помощи бинарного поиска")
my_numbers2 = [1, 2, 3, 5, 7, 11, 12]
print(binary_search(my_numbers, 12))
print("------")
print(binary_search(my_numbers, 7))
print("------")
print(binary_search(my_numbers, 6))
print("------")