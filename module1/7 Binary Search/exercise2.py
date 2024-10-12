def binary_search(nums_list: list[int], target_num: int) -> int:
    left_index = 0
    right_index = len(nums_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = nums_list[mid_index]

        if mid_num == target_num:
            return mid_index
        elif mid_num < target_num:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

if __name__ == "__main__":
    myList = [12, 15, 17, 19, 21, 24, 45, 67]
    target = 45

    index = binary_search(myList, target)
    print(f"Target {target} found at index {index} using Binary search")