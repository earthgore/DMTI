import copy

import N
from MOD_NN_N import MOD_NN_N
from COM_NN_D import COM_NN_D
from NZER_N_B import NZER_N_B


def GCF_NN_N(*nums):
    '''Эта функция находит НОД от произвольного количества элементов
        все элементы nums: N.natural
    '''
    nums = list(copy.deepcopy(nums))
    l = len(nums)
    go = True
    mx = N.natural('1')
    mn = N.natural('0')
    while COM_NN_D(mx,mn) != 0:
        mn_i = 0
        mx_i = 0
        i = 0
        for num in nums:
            if NZER_N_B(num):
                mn_i = i
                mx_i = i
                mn = copy.deepcopy(num)
                mx = copy.deepcopy(num)
                break
            i+=1
        i = 0
        for num in nums:
            if COM_NN_D(mn,num) == 2 and NZER_N_B(num):
                mn_i = i
                mn = copy.deepcopy(num)
            if COM_NN_D(mx,num) == 1:
                mx_i = i
                mx = copy.deepcopy(num)
            i+=1

        if COM_NN_D(mn,mx) != 0:
            nums[mx_i] = MOD_NN_N(mx,mn)
    return mx

