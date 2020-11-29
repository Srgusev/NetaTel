from typing import List


def shift_r(x: List[int]):
    """Выполняет сдвиг вправо списка 'x'
    с заполнением старшего разряда нулём."""
    tmp = []
    tmp.insert(0, x[0])
    for i in range(len(x)-1):
        tmp.insert(i+1, x[i+1])
        x[i+1] = tmp[i]
    x[0] = 0


def ost(e: List[int], m: List[int], g: List[int]):
    """Выполняет операцию нахождения остатка при делении 'm' на 'g' по модулю 2,
    присваивая остаток переменной 'e'.
    Здесь 'e', 'm', 'g' - списки, содержащие коэффициенты соответствующих чисел."""
    n = len(m)
    len_g = len(g)
    len_e = len(e)
    flag = True
    ind = 0  # текущий элемент в m при делении
    while m[ind] == 0:  # сброс ведущих нулей
        ind += 1
        if ind > (n-len_g):
            for i in range(len_g-1):
                e[i] = m[n-(len_g-1-i)]
            return
    while len(e) != len_g:
        e.append(0)
    for i in range(len_g):
        e[i] = m[ind + i]
    while flag:
        i = 0
        while (i < len_g) and ((e[i] ^ g[i]) == 0):
            i += 1
            ind += 1
        tmp = ind
        j = i
        while j < len_g:
            e[j-i] = e[j] ^ g[j]
            tmp += 1
            j += 1
        k = len_g-i
        while k < len_g:
            if tmp > n-1:
                while k < len_g-1:
                    shift_r(e)
                    k += 1
                while len(e) != len_e:
                    e.pop()
                return
            e[k] = m[tmp]
            tmp += 1
            k += 1
