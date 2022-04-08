from nn import *

class integers:
    def __init__(self, str):
        if str[0] == '-':
            str = str.replace('-', '')
            b = 1
        else:
            str = str.replace('+', '')
            b = 0
        self.sign = b
        self.numbers = [int(i) for i in str]
        self.digit = len(str)

    def showInfo(self):
        print(self.sign)
        print(self.numbers)
        print(self.digit)




str0 = input("Введите первое число со знаком + или -:")
z1 = integers(str0)
str01 = input("Введите первое число со знаком + или -:")
z2 = integers(str01)

# Абсолютная величина числа, результат - натуральное ABS_Z_N

def ABS_Z_N1(z1):
    i = 0
    k = 0
    x = 1
    while i < z1.digit:
        k = k + z1.numbers[i] * x
        i = i + 1
        x = x * 10
    k = str(k)
    x = k[::-1]
    print(x)
    return x
zx0 = ABS_Z_N1(z1)
n1_1 = natural(zx0)

def ABS_Z_N2(z2):
    i = 0
    k = 0
    x = 1
    while i < z2.digit:
        k = k + z2.numbers[i] * x
        i = i + 1
        x = x * 10
    k = str(k)
    x = k[::-1]
    print(x)
    return x
zx = ABS_Z_N2(z2)
n1_2 = natural(zx)




def POZ_Z_D(z1):
    if z1.sign == 1:
        return 1
    else:
        i = 0
        k = 0
        while i < z1.digit:
            k = k + z1.numbers[i]
            i = i + 1
        if k == 0:
            return 0
        else:
            return 2


def MUL_ZM_Z(z1):
    i = 0
    k1 = 0
    if z1.sign == 1:
        z1.sign = 0
        k = '+'
    else:
        z1.sign = 1
        k = '-'

    while i < z1.digit:
        k1 = k1 + z1.numbers[i]
        i = i + 1
        if k1 == 0:
            k = ''

    return k


def TRANS_N_Z():
    global z1_1
    st1 = input("Введите первое число:")
    n1 = natural(st1)
    i = 0
    k = 0
    x = 1
    while i < n1.digit:
        k = k + n1.numbers[i]*x
        i = i + 1
        x = x*10
    k = str(k)
    x = k[::-1]
    z1_1 = integers(x)
    return x



def TRANS_Z_N1(z1):
    if z1.sign == 1:
        return 505
    else:
     i = 0
     k = 0
     x = 1
     while i < z1.digit:
        k = k + z1.numbers[i] * x
        i = i + 1
        x = x * 10
    k = str(k)
    x = k[::-1]
    return x



def TRANS_Z_N2(z2):
    if z2.sign == 1:
        return 505
    else:
     i = 0
     k = 0
     x = 1
     while i < z2.digit:
        k = k + z2.numbers[i] * x
        i = i + 1
        x = x * 10
    k = str(k)
    x = k[::-1]
    return x


def ADD_ZZ_Z(z1, z2):
    global n1_1, n1_2
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 2:
        x = ADD_NN_N(n1_1,n1_2)
        x.sign = 0
    elif x1 == x2 and x1 == 0 or x2 == 0:
        if x1 == 0:
            x = z2
        else:
            x = z1
    elif x1 == x2 and x1 == 1:
        x = ADD_NN_N(n1_1,n1_2)
        x.sign = 1

    else:
       k = COM_NN_D(n1_1,n1_2)
       if k == 2 and x1 == 1:
           x = SUB_NN_N(n1_1,n1_2)
           x.sign = 1
       else:
           x = SUB_NN_N(n1_1,n1_2)
           x.sign = 0
    return x


def SUB_ZZ_Z(z1, z2):
    global n1_1, n1_2
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    k = COM_NN_D(n1, n2)
    if x1 == x2 and x1 == 1:
        if k == 2:
            x = SUB_NN_N(n1_1, n1_2)
            x.sign = 1
        else:
            x = SUB_NN_N(n1_2, n1_1)
            x.sign = 0
    elif x1 == x2 and x1 == 2:
       if k == 2:
        x = SUB_NN_N(n1_2, n1_1)
        x.sign = 0
       else:
        x = SUB_NN_N( n1_2, n1_1)
        x.sign = 1
    elif x2 == 1 and x1 == 2:
        x = ADD_NN_N(n1_1,n1_2)
        x.sign = 0
    else:
        x =  ADD_NN_N(n1_1,n1_2)
        x.sign = 1

    x.showInfo()
    return x


def MUL_ZZ_Z(z1, z2):
    global n1_1, n1_2
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 1:
        x = MUL_NN_N(n1_1,n1_2)
        x.sign = 0
    elif x1 == x2 and x1 == 2:
        x = MUL_NN_N(n1_1,n1_2)
        x.sign = 0
    else:
        x = MUL_NN_N(n1_1,n1_2)
        x.sign = 1
    x.showInfo()
    return x


def DIV_ZZ_Z(z1, z2):
    global n1_1, n1_2
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 1:
        x = DIV_NN_N(n1_1,n1_2)
        x.sign = 0
    elif x1 == x2 and x1 == 2:
        x = DIV_NN_N(n1_1,n1_2)
        x.sign = 0
    else:
        x = DIV_NN_N(n1_1,n1_2)
        x.sign = 1
    x.showInfo()
    return x



def MOD_ZZ_Z(z1, z2):
    x = SUB_ZZ_Z(z1, z2 * DIV_ZZ_Z(z1, z2))
    x.sign = 0
    x.showInfo()
    return x

zx = MOD_ZZ_Z(z1, z2)