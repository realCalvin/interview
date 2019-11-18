
def quicksort(nums, low, high):
    if low < high:
        # partition
        pivot = nums[high]
        p1, p2 = low, low
        while p2 < high:
            if nums[p2] > pivot:
                p2 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
        nums[p1], nums[high] = nums[high], nums[p1]

        # recur
        quicksort(nums, low, p1-1)
        quicksort(nums, p1+1, high)
    return nums


def main():
    nums = [4, 7, 8, 1, 2, 3, 9, 5]
    print(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)


if __name__ == '__main__':
    main()

'''
two pointers

[4, 7, 8, 1, 2, 3, 9, 5]
 ^

[4, 7, 8, 1, 2, 3, 9, 5]
    ^

[4, 7, 8, 1, 2, 3, 9, 5]
    ^  ^

[4, 7, 8, 1, 2, 3, 9, 5]
    ^     ^

[4, 1, 8, 7, 2, 3, 9, 5]
       ^     ^

[4, 1, 2, 7, 8, 3, 9, 5]
          ^     ^

[4, 1, 2, 3, 8, 7, 9, 5]
             ^     ^

[4, 1, 2, 3, 5, 7, 9, 8]
             ^        ^


'''
