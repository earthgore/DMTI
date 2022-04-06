import N
from DIV_NN_Dk import DIV_NN_Dk
from SUB_NDN_N import SUB_NDN_N
from COM_NN_D import COM_NN_D
from MUL_Nk_N import MUL_Nk_N
from NZER_N_B import NZER_N_B
import copy


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
    return N.natural(''.join([str(i) for i in array]))

