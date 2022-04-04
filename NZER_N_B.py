import N


# by Maxim Makarov 1308
def NZER_N_B(n):
    '''Эта функция сравнивает n с нулем.
        Возвращает True, если число ненулевое и False, если нулевое.
            n: N.natural
    '''
    for i in n.numbers:
        if i != 0:
            return True
    return False
