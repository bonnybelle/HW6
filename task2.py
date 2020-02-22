# 2. Реализовать RLE сжатие для списка.

nums = [2, 2, 4, 4, 4, 6, 6, 7, 1, 1, 1, 9, 9, 9, 9, 5, 5, 1, 1]


def rle(nums):
    result = []
    i = nums[0]
    count = 1
    for element in nums[1:]:
        if element == i:
            count += 1
        else:
            result.append((i, count))
            count = 1
            i = element
    result.append((i, count))
    return result


print(rle(nums))
