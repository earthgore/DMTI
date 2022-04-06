import N
from DIV_NN_N import DIV_NN_N
from MUL_NN_N import MUL_NN_N
from SUB_NN_N import SUB_NN_N
from COM_NN_D import COM_NN_D
from NZER_N_B import NZER_N_B
import copy

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


