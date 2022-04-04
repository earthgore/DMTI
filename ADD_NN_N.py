import N
from COM_NN_D import COM_NN_D


# by Maxim Makarov 1308
def ADD_NN_N(n1, n2):
    '''Эта функция складывает из числа n1 и n2.
        n1: N.natural
        n2: N.natural
    '''
    k = 0
    if (COM_NN_D(n1, n2) == 1):
        n1, n2 = n2, n1
    n2.numbers = [0] * (n1.digit - n2.digit + 1) + n2.numbers
    n1.numbers = [0] + n1.numbers
    for i in range(n1.digit, -1, -1):
        s = n2.numbers[i] + n1.numbers[i] + k
        n1.numbers[i] = s % 10
        k = s // 10
    if n1.numbers[0] == 0:
        n1.numbers = n1.numbers[1:]
    n1.digit = len(n1.numbers)
    return n1
