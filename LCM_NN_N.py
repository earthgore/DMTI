import copy
import N
from GCF_NN_N import GCF_NN_N
from MUL_NN_N import MUL_NN_N
from DIV_NN_N import DIV_NN_N
from NZER_N_B import NZER_N_B

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
    d = N.natural('1')
    for i in range(1,l):
        s = MUL_NN_N(s,nums[i])
    for i in range(1, l):
        d = MUL_NN_N(d,nod)
    s = DIV_NN_N(s,d)
    return s





