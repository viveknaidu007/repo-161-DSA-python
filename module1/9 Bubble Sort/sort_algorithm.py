def bubble_sort(nums: list[int]) -> list[int]:
    size = len(nums)

    for i in range(size-1):
        # to find out if list is already sorted
        swapped = False
        for j in range(size-1-i):
            if nums[j] > nums[j+1]:
                # Swap the elements
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return nums

nums = [2, 6, 3, 5, 1]
# nums = [1, 4, 6, 9]

sorted_nums = bubble_sort(nums)

print(sorted_nums)