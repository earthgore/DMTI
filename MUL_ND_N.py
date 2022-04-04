import N


# by Maxim Makarov 1308
def MUL_ND_N(a, n):
    '''Эта функция умножает число на цифру.
        если n не является цифрой, вызывает ошибку AssertionError
        a: N.natural
        n: int
    '''
    assert -1 < n < 10
    a.numbers = [0] + [0] + a.numbers
    k = 0
    for i in range(a.digit + 2):
        s = a.numbers[-i] * n + k
        k = s // 10
        a.numbers[-i] = s % 10
    while len(a.numbers) != 0 and a.numbers[0] == 0:
        a.numbers = a.numbers[1:]
    if len(a.numbers) == 0:
        a = N.natural('0')
    a.digit = len(a.numbers)
    return a
