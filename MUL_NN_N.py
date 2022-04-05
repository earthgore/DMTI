import N
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from ADD_NN_N import ADD_NN_N

# by Maxim Makarov 1308
def MUL_NN_N(n1,n2):
    '''Эта функция перемножает числа n1 и n2.
        n1: N.natural
        n2: N.natural
    '''
    s = N.natural('0')
    i = 0
    for elem in n2.numbers[::-1]:
        s = ADD_NN_N(s,MUL_Nk_N(MUL_ND_N(n1,elem),i))
        i+=1
    return s

