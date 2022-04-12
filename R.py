from Z import *



class rational:
    def __init__(self, c, n = natural("1")):
        self.num = c
        self.denum = n

    def __str__(self):
        if(self.num.numbers[0] == 0):
            return "0"
        elif(self.denum.numbers[0] == 0):
            return "Error"
        else:
            if(self.num.sign == 0):
                zn = ''
            else:
                zn = '-'
            return zn + ''.join([str(i) for i in self.num.numbers]) + '/' + ''.join([str(i) for i in self.denum.numbers])
        
    def showInfo(self):
        print(self.num)
        print(self.denum)



def RED_Q_Q(c):
    '''Функция сокращения дробей
    Входные данные: рациональное число'''

    '''НОД числителя и знаменателя'''
    nd = GCF_NN_N(ABS_Z_N(c.num), c.denum)
    if c.num.numbers == [0]:
        return c
    else:
        '''Сокращение на НОД'''
        n1 = DIV_ZZ_Z(c.num, TRANS_N_Z(nd))
        n2 = DIV_NN_N(c.denum, nd)
        return rational(n1, n2)


def INT_Q_B(c):
    '''Функция проверки целое ли число
    Входные данные: рациональное число'''
    
    a = RED_Q_Q(c)
    '''Если знаменатель после сокращения равен единице, значит число целое'''

    if(a.denum.numbers == [1]):
        return True
    else:
        return False


def TRANS_Z_Q(z):
    '''Функция создания рационального числа
    Входные данные : целое число'''
    
    '''Создание знаменателя'''
    n = natural("1")
    c = rational(z, n)
    return c


def TRANS_Q_Z(c):
    '''Функция создания целого числа из дроби
        (знаменатель дроби равен единице)
    Входные данные : рациональное число'''
    c = RED_Q_Q(c)
    if(c.denum.numbers == [1]):
        return c.num
    else:
        raise Exception("DenumError")


def ADD_QQ_Q(a, b):
    '''Функция сложения дробей
    Входные данные : два рациональных числа'''
    nk = MUL_NN_N(a.denum, b.denum)
    nn = ADD_ZZ_Z(MUL_ZZ_Z(a.num, TRANS_N_Z(b.denum)), MUL_ZZ_Z(b.num, TRANS_N_Z(a.denum)))
    c = RED_Q_Q(rational(nn, nk))
    return c


def SUB_QQ_Q(a, b):
    '''Функция вычитания дробей
    Входные данные : два рациональных числа'''
    c = ADD_QQ_Q(a, rational(MUL_ZM_Z(b.num), b.denum))
    return c


def MUL_QQ_Q(a, b):
    '''Функция умножения дробей
    Входные данные : два рациональных числа'''

    '''Знаменатель'''
    c2 = MUL_NN_N(a.denum, b.denum)

    '''Числитель'''
    c1 = MUL_ZZ_Z(a.num, b.num)

    c = RED_Q_Q(rational(c1, c2))
    return c


def DIV_QQ_Q(a, b):
    '''Функция деления дробей
    Входные данные : два рациональных числа'''

    '''Числители дробей'''
    a1 = MUL_ZZ_Z(a.num, TRANS_N_Z(b.denum))

    '''Знаменатели дробей'''
    b1 = MUL_ZZ_Z(TRANS_N_Z(a.denum), b.num)

    if(b1.sign == 1):
        a1 = MUL_ZM_Z(a1)
    c = rational(a1, ABS_Z_N(b1))
    return RED_Q_Q(c)

