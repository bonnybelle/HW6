# 5. Дан список большой вложенности, нужно его развернуть в 1d

lst = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]
temporary_str = str(lst).replace('[', '').replace(']', '')
final = [int(i) for i in temporary_str if i.isdigit()]
print(final)
