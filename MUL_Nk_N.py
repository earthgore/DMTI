import N
import copy


def MUL_Nk_N(n1,k):
    '''Эта функция умножает n на 10^k. k больше или равно 0
        n: N.natural
        k: int
    '''
    n = copy.deepcopy(n1)
    assert k >= 0,"Power can't be negative"
    n.numbers = n.numbers + [0]*k
    n.digit = len(n.numbers)
    return n