
# m4 p1 lvl 1

from random import randint

random_target = randint(0, 100)
random_list = list(set(sorted([randint(0, 100) for i in range(30)])))
print(random_target, random_list)

def binary_search(sorted_list, target, lowest, highest):
    if len(sorted_list) == 0:
        print('Array is empty')
        return -1

    if highest >= lowest:
        mid_index = (highest + lowest) // 2

        if sorted_list[mid_index] == target:
            return mid_index
        elif sorted_list[mid_index] > target:
            return binary_search(sorted_list, target, lowest, mid_index -1)
        elif sorted_list[mid_index] < target:
            return binary_search(sorted_list, target, mid_index + 1, highest)
    else:
        print('There\'s no such item')
        return -1

print(binary_search(random_list, random_target, 0, len(random_list) - 1))

# Alternative option

# import bisect

# def binary_search_native(sorted_list, target):
#     index = bisect.bisect_left(sorted_list, target)
#     if index != len(sorted_list) and sorted_list[index] == target:
#         return index
#     else:
#         print('There\'s no such item')
#         return -1

# print(binary_search_native(random_list, random_target))

# m4 p1 lvl2

from random import randint

random_list1 = [randint(0, 9) for i in range(15)]
print(random_list1)

def insertion_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return -1

    for i in range(1, len(unsorted_list)):
        temp, j = unsorted_list[i], i - 1

        while j >= 0 and temp < unsorted_list[j]:
            unsorted_list[j + 1], j = unsorted_list[j], j - 1
        unsorted_list[j + 1] = temp

insertion_sort(random_list1)
print(random_list1)

# m4 p1 lvl3

from collections import deque

graph = {'A': ['B', 'E'], 
'B': ['A', 'C'],
'C': ['B', 'D'],
'D': ['C'],
'E': ['A', 'F'],
'F': ['E']}
#       A
#   B       E
#   C       F
#   D

def breadth_first_search(graph, start):
    if len(graph) <= 1:
        return -1

    visited = [start]
    queue = deque(start)

    while queue:
        left = queue.popleft()

        for v in graph[left]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

print(breadth_first_search(graph, 'A'))