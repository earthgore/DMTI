import N
from SUB_NN_N import SUB_NN_N
from MUL_ND_N import MUL_ND_N
from COM_NN_D import COM_NN_D
import copy

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

