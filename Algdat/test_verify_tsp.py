#!/usr/bin/python3
# coding=utf-8


def verify_tsp(path, max_weight, weight_matrix):
    weight = 0
    if path[0] != path[-1] or len(set(path[:-1])) != len(path[:-1]):
        return False
    for i in range(len(path)-1):
        weight += weight_matrix[path[i]][path[i+1]] 
    
    return weight <= max_weight

tests = [
    (([1, 0, 0, 1], 187, [[0, 58, 43], [58, 0, 86], [43, 86, 0]]), False),
    (([0, 1, 2, 0], 3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]), True),
    (([0, 2, 1, 3, 0], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([0, 2, 1, 3, 0], 8,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([0, 2, 1, 0], 6,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([0, 2, 1, 3, 0], 6,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([0, 2, 2, 3, 0], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([2, 0, 3, 1, 2], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([2, 0, 3, 1, 3], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False)
]

failed = False

for test_case, answer in tests:
    path, max_weight, weight_matrix = test_case
    student = verify_tsp(path, max_weight, weight_matrix)
    if student != answer:
        print(
            "Koden feilet for følgende input: \npath = {}, ".format(path)
            + "max_weight = {}, ".format(max_weight)
            + "weight_matrix = {}".format(weight_matrix)
        )
        failed = True

if not failed:
    print("Koden fungerte for alle eksempeltestene.")
