import N

def MUL_Nk_N(n,k):
    '''Эта функция умножает n на 10^k. k больше или равно 0
        n: N.natural
        k: int
    '''
    assert k >= 0,"Power can't be negative"
    n.numbers = n.numbers + [0]*k
    n.digit = len(n.numbers)
    return n