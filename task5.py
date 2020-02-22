# 5. Дан список большой вложенности, нужно его развернуть в 1d

lst = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3], 1, 2, 'c', 'b']


def unpack(lst):
    final = []
    for i in lst:
        if type(i) == list:
            final.extend(unpack(i))
        else:
            final.append(i)
    return final


print(unpack(lst))


'''
# Ещё сделала так, но это только для списков с int:

lst = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3], 1, 2, 'c', 'b']
temporary_str = str(lst).replace('[', '').replace(']', '')
final = [int(i) for i in temporary_str if i.isdigit()]
print(final)

Не знаю, что быстрее в таком случае.
'''