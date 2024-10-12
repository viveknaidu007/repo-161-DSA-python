def binary_search(nums_list: list[int], target_num: int) -> int:
    sorted_list = sorted(nums_list)
    left_index = 0
    right_index = len(sorted_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = sorted_list[mid_index]

        if mid_num == target_num:
            return sorted_list, mid_index
        elif mid_num < target_num:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

if __name__ == "__main__":
    myList = [1,4,6,9,10,5,7]
    target = 5

    index = binary_search(myList, target)
    print(f"Target {target} found in the sorted list {index[0]} at index {index[1]} using Binary search")