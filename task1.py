# 1. Найти самую длинную последовательность из одинаковых чисел в списке, вывести длину и само число.
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
# '9' - 4
nums = [2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]


def longest_sequence(nums):
    actual = {}
    final = {}
    count = 0
    for x in range(len(nums) - 1):
        if nums[x] == nums[x + 1]:
            count += 1
            # temporary_dict = {nums[x]: count}
            # actual.update(temporary_dict)
            actual[nums[x]] = count
            if count > actual.get(nums[x]):
                actual[nums[x]] = count
            # actual.get(nums[x])
        elif nums[x] != nums[x + 1]:
            count = 1
            final[nums[x]] = count
            final.update(actual)
    max_value = max(final.values())
    max_keys = [k for k, v in final.items() if v == max_value]
    temporary_dict = {nums[-1]: count}
    for k, v in temporary_dict.items():
        if v > max_value:
            return ''.join(('Число: ', str(k), '\nКоличество: ', str(v)))
        elif v < max_value:
            return ''.join(('Число: ', str(max_keys)[1], '\nКоличество: ', str(max_value)))


print(longest_sequence(nums))
