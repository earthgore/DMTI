
from copy import copy

class natural:
    def __init__(self, str = ""):
        self.numbers = [int(i) for i in str]
        self.digit = len(str)

    def __str__(self):
        return ''.join([str(i) for i in self.numbers])

    def showInfo(self):
        print(self.numbers)
        print(self.digit)

import copy

# COM_NN_D_by_Antom_Muraveov_&_Alexandr_Varfolomeev_1308
def COM_NN_D(a, b):
    if a.digit > b.digit:
        """Если число разрядов a больше числа разрядов b, сразу возращаем 2"""
        return 2
    elif a.digit == b.digit:
        """Если число разрядов a равно числу разрядов b, сравниваем цифры поразрядно. Если все цифры равны, возвращаем 0"""
        i = 0
        while a.numbers[i] == b.numbers[i] and i < a.digit:
            if i + 1 == a.digit and a.numbers[i] == b.numbers[i]:
                return 0
            i = i + 1
        """Если цифра числа a больше цифры числа b, возвращаем 2"""
        if a.numbers[i] > b.numbers[i]:
            return 2
    return 1

# by Maxim Makarov 1308
def SUB_NN_N(n1, n2):
    '''Эта функция вычитает из числа n1 число n2.
        Если n1<n2 вызывает ошибку AssertionError.
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n1)
    n2 = copy.deepcopy(n2)

    k = 0
    assert COM_NN_D(n1, n2) == 2 or COM_NN_D(n1, n2) == 0
    n2.numbers = [0] * (n1.digit - n2.digit) + n2.numbers
    if COM_NN_D(n1, n2) == 0:
        return natural('0')
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

def SUB_NDN_N(n11,n21,k):
    '''Эта функция вычитает из числа n11 число n21 умноженное на цифру k.
        Если n1<n2 вызывает ошибку AssertionError.
        n11: N.natural
        n21: N.natural
        k: int
    '''
    assert 0<=k<=9, "K should be a single digit"
    n1 = copy.deepcopy(n11)
    n2 = copy.deepcopy(n21)
    n2 = MUL_ND_N(n2,k)
    assert COM_NN_D(n1,n2) == 2 or COM_NN_D(n1,n2) == 0, "Result will be negative"
    n1 = SUB_NN_N(n1,n2)
    return n1

# by Maxim Makarov 1308
def NZER_N_B(n):
    '''Эта функция сравнивает n с нулем.
        Возвращает True, если число ненулевое и False, если нулевое.
            n: N.natural
    '''
    for i in n.numbers:
        if i != 0:
            return True
    return False

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


# by Maxim Makarov 1308
def MUL_NN_N(n1,n2):
    '''Эта функция перемножает числа n1 и n2.
        n1: N.natural
        n2: N.natural
    '''
    s = natural('0')
    i = 0
    for elem in n2.numbers[::-1]:
        s = ADD_NN_N(s,MUL_Nk_N(MUL_ND_N(n1,elem),i))
        i+=1
    return s


# by Maxim Makarov 1308
def MUL_ND_N(a1, n):
    '''Эта функция умножает число на цифру.
        если n не является цифрой, вызывает ошибку AssertionError
        a: N.natural
        n: int
    '''
    a = copy.deepcopy(a1)
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
        a = natural('0')
    a.digit = len(a.numbers)
    return a


def MOD_NN_N(n1,n2):
    '''Эта функция находит остаток от деления n1 на n2
        n2 больше нуля
        n2 меньше или равно n1
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n1)
    n2 = copy.deepcopy(n2)
    assert COM_NN_D(n1, n2) != 1, 'first number should be bigger than the second or equal'
    assert NZER_N_B(n2), 'zero division'
    n3 = DIV_NN_N(n1,n2)
    n4 = SUB_NN_N(n1,MUL_NN_N(n3,n2))
    return n4


def LCM_NN_N(*nums):
    '''Эта функция находит НОК от произвольного количества элементов
        все элементы nums: N.natural
    '''
    for i in nums:
        assert NZER_N_B(i), 'You cant use zero in this function'
    assert len(nums)!= 0,'Should be at least 1 number'
    if len(nums) == 1:
        return nums[0]
    nod = GCF_NN_N(*nums)
    l = len(nums)
    s = copy.deepcopy(nums[0])
    d = natural('1')
    for i in range(1,l):
        s = MUL_NN_N(s,nums[i])
    for i in range(1, l):
        d = MUL_NN_N(d,nod)
    s = DIV_NN_N(s,d)
    return s

def GCF_NN_N(*nums):
    '''Эта функция находит НОД от произвольного количества элементов
        все элементы nums: N.natural
    '''
    nums = list(copy.deepcopy(nums))
    l = len(nums)
    go = True
    mx = natural('1')
    mn = natural('0')
    while COM_NN_D(mx,mn) != 0:
        mn_i = 0
        mx_i = 0
        i = 0
        for num in nums:
            if NZER_N_B(num):
                mn_i = i
                mx_i = i
                mn = copy.deepcopy(num)
                mx = copy.deepcopy(num)
                break
            i+=1
        i = 0
        for num in nums:
            if COM_NN_D(mn,num) == 2 and NZER_N_B(num):
                mn_i = i
                mn = copy.deepcopy(num)
            if COM_NN_D(mx,num) == 1:
                mx_i = i
                mx = copy.deepcopy(num)
            i+=1

        if COM_NN_D(mn,mx) != 0:
            nums[mx_i] = MOD_NN_N(mx,mn)
    return mx


def DIV_NN_N(n1,n2):
    '''Эта функция находит частное от деления n1 на n2
        n2 больше нуля
        n2 меньше или равно n1
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n1)
    n2 = copy.deepcopy(n2)
    assert COM_NN_D(n1, n2) != 1, 'first number should be bigger than the second or equal'
    assert NZER_N_B(n2),'zero division'
    array = []
    k = n1.digit-n2.digit+1
    while  k>-1:
        if COM_NN_D(n1,MUL_Nk_N(n2,k)) == 1:
            array.append(0)
        else:
            n = DIV_NN_Dk(n1,n2)
            array.append(n)
            n1 = SUB_NDN_N(n1,MUL_Nk_N(n2,k),n)
        k-=1
    while array[0] == 0:
        array = array[1:]
    return natural(''.join([str(i) for i in array]))


# by maxim makarov 1308
def DIV_NN_Dk(n1, n2):
    ''' Эта функция находит первую цифру частного от деления n1 на n2
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n1)
    n2 = copy.deepcopy(n2)
    k = natural('0')
    i = 0
    assert COM_NN_D(n1, n2) != 1, 'first number should be bigger than the second or equal'
    if n1.digit - n2.digit != 0:
        n2 = MUL_Nk_N(n2, n1.digit - n2.digit - 1)
        if COM_NN_D(n1, MUL_Nk_N(n2, 1)) != 1:
            n2 = MUL_Nk_N(n2, 1)
    while COM_NN_D(n1, ADD_NN_N(n2, k)) != 1:
        i += 1
        k = ADD_NN_N(n2, k)
    return i




# by Maxim Makarov 1308
def ADD_NN_N(n11, n21):
    '''Эта функция складывает числа n1 и n2.
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n11)
    n2 = copy.deepcopy(n21)
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
def ADD_1N_N(n1):
    '''Эта функция прибавляет единицу к n.
        n: N.natural
    '''
    n = copy.deepcopy(n1)
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



st1 = input("Введите первое число:")
st2 = input("Введите второе число:")
n1 = natural(st1)
n2 = natural(st2)