
def mergesort(nums):
    if len(nums) > 1:
        # partition
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        # recur until size is 1
        mergesort(left)
        mergesort(right)

        # merge together
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1


def main():
    nums = [4, 7, 8, 1, 2, 3, 9, 5]
    print(nums)
    mergesort(nums)
    print(nums)


if __name__ == '__main__':
    main()
