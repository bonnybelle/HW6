# 6. Дан список из чисел. Нужно реализовать подсчет суммы чисел на отрезке списка. На вход даются запросы в виде пары
# чисел - индекс начала и конца интервала для суммирования - нужно выводить сумму элементов списка для каждого запроса.

nums = [1, 21, -23, 245, 88, 234, 0, 0, -1, -98, 44, 19, 9, 2, 3, -3]
while True:
    start = int(input('Индекс начала: '))
    finish = int(input('Индекс конца: '))
    result = sum(nums[start:finish+1])
    print('Сумма чисел на отрезке:', result)