from Algorithms.ost import ost
from typing import List


def invers(x: int) -> int:
    """Возвращает выполнение операции инверсия к биту x."""
    assert 0 <= x <= 1
    if x == 1:
        return 0
    else:
        return 1


def _calc(m: List[int], g: List[int]) -> int:
    """Возвращает результат обнаружения ошибки.
    1 - ошибка обнаружена, 0 - ошибка не обнаружена."""
    e, reference = [], []
    for i in range(len(g)-1):
        e.append(0)
        reference.append(0)
    ost(e, m, g)
    if e != reference:
        return 1
    else:
        return 0


def c_1(m: List[int], g: List[int], count = 0, comb = 0, j = 0) -> (int, int):
    """Выполняет генерацию ошибок 1-й кратности.
    Принимает параметры: m - проверяемый вектор;
    g - порождающий полином.
    Возвращает количество обнаруженных
    ошибок; общее количество сгенерированных ошибок
    для кратности 1 соответственно."""
    n = len(m)
    for i in range(j, n):
        m[i] = invers(m[i])
        comb += 1
        count += _calc(m, g)
        m[i] = invers(m[i])
    return count, comb


def c_k(m: List[int], g: List[int], k: int, count=0, comb=0, j=0) -> (int, int):
    """Выполняет генерацию ошибок (k+1)-й кратности.
    Принимает параметры: m - проверяемый вектор;
    g - порождающий полином; k - кратность ошибки
    без единицы.
    Возвращает количество обнаруженных
    ошибок; общее количество сгенерированных ошибок
    для кратности (k+1) соответственно."""
    n = len(m)
    for i in range(j, n-k+1):
        m[i] = invers(m[i])
        if k == 1:
            count, comb = c_1(m, g, count, comb, i+1)
        else:
            count, comb = c_k(m, g, k-1, count, comb, i+1)
        m[i] = invers(m[i])
    return count, comb
