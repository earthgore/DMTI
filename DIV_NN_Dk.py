import N
from MUL_Nk_N import MUL_Nk_N
from COM_NN_D import COM_NN_D
from ADD_NN_N import ADD_NN_N

import copy


# by maxim makarov 1308
def DIV_NN_Dk(n1, n2):
    ''' Эта функция находит первую цифру частного от деления n1 на n2
        n1: N.natural
        n2: N.natural
    '''
    n1 = copy.deepcopy(n1)
    n2 = copy.deepcopy(n2)
    k = N.natural('0')
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
