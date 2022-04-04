import N


# COM_NN_D_by_Antom_Muraveov
def COM_NN_D(a, b):
    if a.digit > b.digit:
        """Если число разрядов a больше числа разрядов b, сразу возращаем 2"""
        return 2
    elif a.digit == b.digit:
        """Если число разрядов a равно числу разрядов b, сравниваем цифры поразрядно. Если все цифры равны, возвращаем 0"""
        i = 0
        while a.numbers[i] == b.numbers[i] and i < a.digit:
            if i + 1 == a.digit and a.numbers[i] == b.numbers[i]:
                return 0
            i = i + 1
        """Если цифра числа a больше цифры числа b, возвращаем 2"""
        if a.numbers[i] > b.numbers[i]:
            return 2
    return 1
