from N import *
from copy import copy

class integers:
    def __init__(self, str  = ""):
        if str == "":
            b = 0
        elif str[0] == '-':
            str = str.replace('-', '')
            b = 1
        else:
            str = str.replace('+', '')
            b = 0
        self.sign = b
        self.numbers = [int(i) for i in str]
        self.digit = len(str)


    def __str__(self):
        if self.sign == 1:
            c = '-'
        else:
            c = ''
        return c + ''.join([str(i) for i in self.numbers])


    def showInfo(self):
        print(self.sign)
        print(self.numbers)
        print(self.digit)




str0 = input("Введите первое число со знаком + или -:")
z1 = integers(str0)
str01 = input("Введите второе число со знаком + или -:")
z2 = integers(str01)

#ABS_Z_N_by_Alexandr_Varfolomeev_1308
def ABS_Z_N(z):
    """
    Функция получает на вход целое число любого знака,
    на выходе получается натуральное число.
    """
    n = natural()
    n.numbers = copy(z.numbers)
    n.digit = len(n.numbers)
    return n
n1_1 = ABS_Z_N(z1)
n1_2 = ABS_Z_N(z2)

#POZ_Z_D_by_Antom_Muraveov_1308
def POZ_Z_D(z1):
    """
    Функция получает на вход целое число любого знака,
    определяет положительность числа.
    Выход - 2 - положительное, 0 — равное нулю, 1 - отрицательное
    """
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

#MUL_ZM_Z_by_Antom_Muraveov_1308
def MUL_ZM_Z(z1):
    """
    Функция получает на вход целое число любого знака.
    Функция проверяет знак и меняет его на проивоположный.

    """
    if z1.sign == 1:
        z1.sign = 0
    else:
        z1.sign = 1
    return z1


#TRANS_N_Z_by_Alexandr_Varfolomeev_1308
def TRANS_N_Z(n1):
    """
    Функция получает на вход одно натуральное число.
    Преобразует натуральное число в целое
           копированием из одного класса в другой.
        """
    z = integers()
    z.numbers = copy(n1.numbers)
    z.digit = n1.digit
    z.sign = 0
    return z

#TRANS_Z_N_by_Antom_Muraveov_1308
def TRANS_Z_N(z1):
    """
    Функция получает на вход целое число положительного знака.
    Используя функцию модуля коныертирует натуральный тип
       в целочисленный.
    Если на вход отрицательное число, то программа выдаст ошибку.
        """
    if z1.sign == 1:
        return 505
    else:
        return ABS_Z_N(z1)

#ADD_ZZ__by_Antom_Muraveov_1308
def ADD_ZZ_Z(z1, z2):
    """
    Функция получает на вход два целых числа любого знака.
    После конвертации чисел в натуральные, происходят операции
      сложения и вычитания из блока натуральных чисел.
        """
    n1 = ABS_Z_N(z1)
    n2 = ABS_Z_N(z2)
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 2:
        """Если оба числа положительные, то они просто скаладываются"""
        return TRANS_N_Z(ADD_NN_N(n1,n2))

    elif x1 == x2 and x1 == 1:
        """Если оба числа отрицательные, то они скалдваются и у суммы меняется знак"""
        return MUL_ZM_Z(TRANS_N_Z(ADD_NN_N(n1,n2)))
    elif x1 == 0:
        """Если первое число равно нулю - возвращается второе"""
        return z2
    elif x2 == 0:
        """Если второе число равно нулю = возвращается первое"""
        return z1
    else:
       k = COM_NN_D(n1,n2)
       if k == 2 and x1 == 1:
           """Если первое число больше второго и при этом оно отрицательное, то возвращается их разность и меняется знак"""
           return MUL_ZM_Z(TRANS_N_Z(SUB_NN_N(n1,n2)))
       elif k == 2 and x2 == 1:
           """Если первое число больше второго, а второе число отрицательное, то возвращается их разность"""
           return TRANS_N_Z(SUB_NN_N(n1, n2))
       elif k != 2 and x2 == 1:
           """Если первое число не больше второго, а второе число отрицательное, то возвращается их разность с обратным знаком"""
           return MUL_ZM_Z(TRANS_N_Z(SUB_NN_N(n2,n1)))
       else:
           """Во всех остальных случаях - разность второго и первого числа с обратным знаком"""
           return TRANS_N_Z(SUB_NN_N(n2,n1))


#SUB_ZZ_Z_by_Antom_Muraveov_1308
def SUB_ZZ_Z(z1, z2):
    """
    Функция получает на вход два целых числа любого знака.
    После конвертации чисел в натуральные, происходят операции
      сложения и вычитания из блока натуральных чисел.

        """
    n1 = ABS_Z_N(z1)
    n2 = ABS_Z_N(z2)
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    k = COM_NN_D(n1_1, n1_2)
    if x1 == x2 and x1 == 1:
        if k == 2:
            """Если оба числа отрицательные и первое число больше второго, возвращается их разность с противоположным знаком"""
            return MUL_ZM_Z(TRANS_N_Z(SUB_NN_N(n1, n2)))

        else:
            """Если оба числа отрицательные и второе число больше первого, возвращается разность второго и первого"""
            return TRANS_N_Z(SUB_NN_N(n2, n1))
    elif x2 == x1 and x1 == 0:
        """Если оба числа отрицательные, то возвращается нуль"""
        return integers("0")
    elif x1 == 0 and x2 != 0:
        """Если первое чсило нулевое, а второе не нулевое, то возвращается второе число с пртивоположным знаком"""
        return MUL_ZM_Z(z2)
    elif x1 != 0 and x2 == 0:
        """Если первое число не нулевое, а второе нулевое, то возвращается первое число"""
        return z1
    elif x1 == x2 and x1 == 2:
       if k == 2:
        """Если оба числа положительные и первое больше второго, возвращается их разность"""
        return TRANS_N_Z(SUB_NN_N(n1, n2))
       else:
        """Если оба числа положительные и второе больше первого, возвращается разность второго и ервого с обратным знаком"""
        return  MUL_ZM_Z(TRANS_N_Z(SUB_NN_N(n2, n1)))
    elif x1 == 2 and x2 == 1:
        """Если первое число положительное, а второе отрицательно, то возвращается их сумма"""
        return TRANS_N_Z(ADD_NN_N(n1,n2))

    else:
        """Во всех остальных случаях - возвращается сумма с обратным знаком"""
        return MUL_ZM_Z(TRANS_N_Z(ADD_NN_N(n1,n2)))



#MUL_ZZ_Z_by_Antom_Muraveov_1308
def MUL_ZZ_Z(z1, z2):
    """
    Функция получает на вход два целых числа любого знака.
    После конвертации чисел в натуральные, происходят операции
      сложения и вычитания из блока натуральных чисел.
        """
    n1 = ABS_Z_N(z1)
    n2 = ABS_Z_N(z2)
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 1:
        """Если оба числа положительные, то проиходит их умножение"""
        return TRANS_N_Z(MUL_NN_N(n1,n2))

    elif x1 == x2 and x1 == 2:
        """Если оба числа отрицательные, то проиходит их умножение"""
        return TRANS_N_Z(MUL_NN_N(n1,n2))

    else:
        """Во всех остальных случаях - умножение с обратным знаком"""
        return MUL_ZM_Z(TRANS_N_Z(MUL_NN_N(n1,n2)))


#DIV_ZZ_Z_by_Antom_Muraveov_1308
def DIV_ZZ_Z(z1, z2):
    """
    Функция получает на вход два целых числа любого знака.
    После конвертации чисел в натуральные, происходят операции
      сложения и вычитания из блока натуральных чисел.
        """
    n1 = ABS_Z_N(z1)
    n2 = ABS_Z_N(z2)
    x1 = POZ_Z_D(z1)
    x2 = POZ_Z_D(z2)
    if x1 == x2 and x1 == 1:
         """Если оба числа положительные, то проиходит их деление"""
         return TRANS_N_Z(DIV_NN_N(n1,n2))

    elif x1 == x2 and x1 == 2:
        """Если оба числа отрицательные, то проиходит их деление"""
        return TRANS_N_Z(DIV_NN_N(n1,n2))
    else:
        """Во всех остальных случаях - деление с обратным знаком"""
        return MUL_ZM_Z(TRANS_N_Z(DIV_NN_N(n1,n2)))


#MOD_ZZ_Z_by_Antom_Muraveov_1308
def MOD_ZZ_Z(z1, z2):
    """
    Функция получает на вход два целых числа любого знака.
    Используя формулу a = b * q + r,  где r - остаток,выражается r
        """
    return SUB_ZZ_Z(z1, MUL_ZZ_Z(z2, DIV_ZZ_Z(z1, z2)))
