import N


# by Maxim Makarov 1308
def ADD_1N_N(n):
    '''Эта функция прибавляет единицу к n.
        n: N.natural
    '''
    i = 1
    n.numbers = [0] + n.numbers
    while n.numbers[-i] == 9:
        n.numbers[-i] = 0
        i += 1
    n.numbers[-i] += 1
    if n.numbers[0] == 0:
        n.numbers = n.numbers[1:]
    n.digit = len(n.numbers)
    return n
