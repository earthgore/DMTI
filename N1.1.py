class natural:
    def __init__(self, str):
        self.numbers = [int(i) for i in str]
        self.digit = len(str)



#COM_NN_D_by_Antom_Muraveov_1308_&_Alexandr_Varfolomeev_1308
def COM_NN_D(n1,n2):
    if n1.digit > n2.digit:
        """Если число разрядов a больше числа разрядов b, сразу возращаем 2"""
        return 2
    elif n1.digit == n2.digit:
        """Если число разрядов a равно числу разрядов b, сравниваем цифры поразрядно. Если все цифры равны, возвращаем 0"""
        i = 0
        while n1.numbers[i] == n2.numbers[i] and i < n1.digit:
            if i + 1 == n1.digit and n1.numbers[i] == n2.numbers[i]:
                return 0
            i = i + 1
        """Если цифра числа a больше цифры числа b, возвращаем 2"""
        if n1.numbers[i] > n2.numbers[i]:
            return 2
    return 1


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


# by Maxim Makarov 1308
def SUB_NN_N(n1, n2):
    '''Эта функция вычитает из числа n1 число n2.
        Если n1<n2 вызывает ошибку AssertionError.
        n1: N.natural
        n2: N.natural
    '''
    k = 0
    assert COM_NN_D(n1, n2) == 2 or COM_NN_D(n1, n2) == 0
    n2.numbers = [0] * (n1.digit - n2.digit) + n2.numbers
    if COM_NN_D(n1, n2) == 0:
        return n1.natural('0')
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


# by Maxim Makarov 1308
def NZER_N_B(n1):
    '''Эта функция сравнивает n с нулем.
        Возвращает True, если число ненулевое и False, если нулевое.
            n: N.natural
    '''
    for i in n1.numbers:
        if i != 0:
            return True
    return False


# by Maxim Makarov 1308
def MUL_ND_N(n1, n):
    '''Эта функция умножает число на цифру.
        если n не является цифрой, вызывает ошибку AssertionError
        a: N.natural
        n: int
    '''
    assert -1 < n < 10
    n1.numbers = [0] + [0] + n1.numbers
    k = 0
    for i in range(n1.digit + 2):
        s = n1.numbers[-i] * n + k
        k = s // 10
        n1.numbers[-i] = s % 10
    while len(n1.numbers) != 0 and n1.numbers[0] == 0:
        n1.numbers = n1.numbers[1:]
    if len(n1.numbers) == 0:
        n1 = n1.natural('0')
    n1.digit = len(n1.numbers)
    return n1


def ADD_1N_N(n1):
    '''Эта функция прибавляет единицу к n.
        n: N.natural
    '''
    i = 1
    n1.numbers = [0] + n1.numbers
    while n1.numbers[-i] == 9:
        n1.numbers[-i] = 0
        i += 1
    n1.numbers[-i] += 1
    if n1.numbers[0] == 0:
        n1.numbers = n1.numbers[1:]
    n1.digit = len(n1.numbers)
    return n1




n = int(input("Введите цифру:"))
st1 = input("Введите первое число:")
st2 = input("Введите второе число:")
n1 = natural(st1)
n2 = natural(st2)

d1 = COM_NN_D(n1, n2)
d2 = ADD_NN_N(n1, n2)
d3 = SUB_NN_N(n1, n2)
d4 = NZER_N_B(n1)
d5 = MUL_ND_N(n1, n)
d6 = ADD_1N_N(n1)

qw = input("Введите 1 если:COM_NN_D,Введите 2 если:ADD_NN_N,Введите 3 если:SUB_NN_N,Введите 4 если:NZER_N_B,Введите 5 если:MUL_ND_N,Введите 6 если:ADD_1N_N")
if qw == 1:
    print(d1)
elif qw == 2:
    print(d2)
elif qw == 3:
    print(d3)
elif qw == 4:
    print(d4)
elif qw == 5:
    print(d5)
elif qw == 6:
    print(d6)


