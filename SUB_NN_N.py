import N
from COM_NN_D import COM_NN_D
import copy

# by Maxim Makarov 1308
def SUB_NN_N(n11, n21):
    '''Эта функция вычитает из числа n1 число n2.
        Если n1<n2 вызывает ошибку AssertionError.
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n11)
    n2 = copy.deepcopy(n21)

    k = 0
    assert COM_NN_D(n1, n2) == 2 or COM_NN_D(n1, n2) == 0
    n2.numbers = [0] * (n1.digit - n2.digit) + n2.numbers
    if COM_NN_D(n1, n2) == 0:
        return N.natural('0')
    else:
        for i in range(n1.digit - 1, -1, -1):
            s = n1.numbers[i] - n2.numbers[i] + k
            if s < 0:
                k = -1
            else:
                k = 0
            n1.numbers[i] = s % 10
    while n1.numbers[0] == 0:
        n1.numbers = n1.numbers[1:]
    n1.digit = len(n1.numbers)
    return n1
