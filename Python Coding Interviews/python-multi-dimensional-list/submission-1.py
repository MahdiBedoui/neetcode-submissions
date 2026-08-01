from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    list_max = []
    for i in range(len(nested_arr)):
        maxi = nested_arr[i][0]
        for j in range(len(nested_arr[i])):
            if maxi < max (maxi, nested_arr[i][j]):
                maxi = nested_arr[i][j]
        list_max.append(maxi) 
    return list_max
    pass


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
