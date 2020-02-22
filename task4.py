# 4. Поиск минимума с переменным числом аргументов в списке.


def min(*args):
    args_lst = [i for i in args]
    minimum = args_lst[0]
    for j in range(len(args_lst) - 1):
        if minimum > args_lst[j]:
            minimum = args_lst[j]
    return 'minimum: {} from args: {}'.format(minimum, args_lst)


print(min(0, 9, -28, 45, 9, 0, 1, 2, 123),
      min(4, 7, 3, 4, 5, 6),
      sep='\n')
