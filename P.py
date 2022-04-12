from R import *



class polynom:
    def __init__(self, a = [rational(integers("0"))]):
        self.digit = len(a) - 1
        self.coe = a

    def __str__(self):
        c = ""
        for i in range(self.digit):
            if INT_Q_B(self.coe[i]):
                if POZ_Z_D(self.coe[i].num) == 1:
                    c += "(" + str(TRANS_Q_Z(self.coe[i])) + ")" + "x^" + str(self.digit - i) + "+"
                else:
                    c += str(TRANS_Q_Z(self.coe[i])) + "x^" + str(self.digit - i) + "+"
            else:
                c += "(" + str(self.coe[i]) + ")" + "x^" + str(self.digit - i) + "+"

        if INT_Q_B(self.coe[-1]):
            if POZ_Z_D(self.coe[-1].num) == 1:
                c += "(" + str(TRANS_Q_Z(self.coe[-1])) + ")"
            else:
                c += str(TRANS_Q_Z(self.coe[-1]))
        else:
            c += "(" + str(self.coe[-1]) + ")"
        return c


def ADD_PP_P(a, b):
    '''Сложение многочленов'''
    '''Выбираем многочлен с большей степенью'''
    if a.digit >= b.digit:
        a1 = a
        b1 = b
    else:
        a1 = b
        b1 = a
    c = []
    d = a1.digit - b1.digit
    '''Складываем соответствующие коэффициенты'''
    for i in range(a1.digit + 1):
        if i < d:
            c.append(a1.coe[i])
        else:
            c.append(ADD_QQ_Q(a1.coe[i], b1.coe[i - d]))
    return polynom(c)

def SUB_PP_P(a, b):
    '''Вычитание многочленов'''
    '''Умножаем все коэффициенты второго многочлена на минус один и складываем многочлены'''
    c = [MUL_QQ_Q(rational(integers("-1")), i) for i in b.coe]
    return (ADD_PP_P(a, polynom(c)))

def MUL_PQ_P(a, x):
    '''Умножение многочлена на рациональное число'''
    '''Умножаем все коэффициенты многочлена на рациональное число'''
    c = [MUL_QQ_Q(x, i) for i in a.coe]
    return polynom(c)

def MUL_Pxk_P(a, k):
    '''Умножение многочлена на x^k'''
    '''Сдвигаем коэффициенты на k влево, путём добавления нулевых коэффициентов справа'''
    for i in range(k):
        a.coe.append(rational(integers("0")))
    a.digit += k
    return a

def LED_P_Q(a):
    '''Старший коэффициент многочлена'''
    return a.coe[0]

def DEG_P_N(a):
    '''Степень многочлена'''
    return a.digit

def FAC_P_Q(a):
    '''Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей'''
    '''Находим НОД числителей и НОК знаменателей всех коэффициентов'''
    nk = a.coe[0].denum
    nd = TRANS_Z_N(a.coe[0].num)
    for i in range(a.digit):
        nk = LCM_NN_N(nk, a.coe[i + 1].denum)
        nd = GCF_NN_N(nd, TRANS_Z_N(a.coe[i + 1].num))
    '''Домножаем все коэффициенты на НОК и делим на НОД'''
    c = [RED_Q_Q(MUL_QQ_Q(i, rational(TRANS_N_Z(nk), nd))) for i in a.coe]
    return polynom(c)

def MUL_PP_P(a, b):
    '''Умножение многочленов'''
    c = polynom()
    '''Для всех коэффициентов b прибавляем к c произведение a на коэффициент b умноженный на x в соответствующей степени'''
    for i in range(b.digit + 1):
        c = ADD_PP_P(c, MUL_Pxk_P(MUL_PQ_P(a, b.coe[i]), b.digit - i))
    return c

def DIV_PP_P(a, b):
    '''Частное от деления многочлена на многочлен при делении с остатком'''
    c = []
    n = a.digit - b.digit
    '''Пока a >= b вычитаем из a произведение b на частное 
    от деления старшего коэффициента a на старший коэффициент b умноженное на x в соответствующей степени'''
    for i in range(n + 1):
        if a.coe[0].num.numbers != [0]:
            c.append(DIV_QQ_Q(a.coe[0], b.coe[0]))
            a = SUB_PP_P(a, MUL_Pxk_P(MUL_PQ_P(b, c[i]), n - i))
        else:
            c.append(rational(integers("0")))
        a.coe.pop(0)
        a.digit -= 1
    while a.digit > 0 and a.coe[0].num.numbers == [0]:
        a.coe.pop(0)
        a.digit -= 1
    return polynom(c)

def MOD_PP_P(a, b):
    '''Остаток от деления многочлена на многочлен при делении с остатком'''
    c = []
    n = a.digit - b.digit
    '''Пока a >= b вычитаем из a произведение b на частное 
        от деления старшего коэффициента a на старший коэффициент b умноженное на x в соответствующей степени'''
    for i in range(n + 1):
        if a.coe[0].num.numbers != [0]:
            c.append(DIV_QQ_Q(a.coe[0], b.coe[0]))
            a = SUB_PP_P(a, MUL_Pxk_P(MUL_PQ_P(b, c[i]), n - i))
        else:
            c.append(rational(integers("0")))
        a.coe.pop(0)
        a.digit -= 1
    while a.digit > 0 and a.coe[0].num.numbers == [0]:
        a.coe.pop(0)
        a.digit -= 1
    return a

def DER_P_P(a):
    '''Производная многочлена'''
    c = [MUL_QQ_Q(a.coe[i], rational(integers(str(a.digit - i)))) for i in range(a.digit)]
    return polynom(c)

def COM_PP_P(a, b):
    '''Проверка на равенство многочленов'''
    count = 0
    if a.digit == b.digit:
        for i in range(a.digit + 1):
            if a.coe[i].num.numbers == b.coe[i].num.numbers and a.coe[i].denum.numbers == b.coe[i].denum.numbers:
                count += 1
    else:
        return False
    if count == a.digit + 1:
        return True
    else:
        return False

def GCF_PP_P(a, b):
    '''НОД многочленов'''
    '''Выбираем многочлен с большей степенью'''
    if a.digit >= b.digit:
        a1 = a
        b1 = b
    else:
        a1 = b
        b1 = a
    tmp = b1
    '''Делим с остатком делитель предыдущего шага на остаток предыдущего шага, пока остаток не равен нулю или константе'''
    while COM_PP_P(b1, polynom()) == False:
        tmp = b1
        b1 = MOD_PP_P(a1, b1)
        a1 = tmp
        if b1.digit < 1 and COM_PP_P(b1, polynom()) == False:
            return polynom([rational(integers("1"))])
    '''Возвращаем последний ненулевой остаток или единицу'''
    return tmp

def NMR_P_P(a):
    '''Преобразование многочлена — кратные корни в простые'''
    '''Делим многочлен на НОД мночлена и его производной, чтобы избавится от корней кратности выше единицы'''
    return DIV_PP_P(a, GCF_PP_P(a, DER_P_P(a)))


"""#a = [rational(integers(i.split("/")[0]), natural(i.split("/")[1])) for i in input("Введите первый многочлен: ").split()]
#b = [rational(integers(i.split("/")[0]), natural(i.split("/")[1])) for i in input("Введите второй многочлен: ").split()]
a = [rational(integers(i)) for i in input("Введите второй многочлен: ").split()]
b = [rational(integers(i)) for i in input("Введите второй многочлен: ").split()]
#c = [rational(integers(i)) for i in input("Введите второй многочлен: ").split()]
#d = [rational(integers(i)) for i in input("Введите второй многочлен: ").split()]
'''c = rational(integers(input("Введите число: ")))
d = int(input("Введите степень: "))'''
a = polynom(a)
b = polynom(b)
#c = polynom(c)
#d = polynom(d)

print(GCF_PP_P(a, b))
print(NMR_P_P(a))"""
