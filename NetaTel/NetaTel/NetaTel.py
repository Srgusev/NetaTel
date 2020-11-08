#Реализация циклического кода [7,4]   ДЗ2   Сети и телекоммуникации 
 
import math
def division (ostatok, divider):
    while int.bit_length(ostatok) >= int.bit_length(divider):
        sub=divider
        while not(int.bit_length(ostatok) == int.bit_length(sub)): sub<<=1
        ostatok^=sub
    return ostatok
def print_bin(bin_num):
    bin_num=str(bin(bin_num))
    bin_num=bin_num[2:len(bin_num):1]
    print(bin_num.rjust(7, "0"))
inform_vector=0b0100 # Заданный информационный вектор
p_polinom=0b1011 # g(x) = х^3+х+1
fixed_errors=[0, 0, 0, 0, 0, 0, 0]# Исправленные ошибки
prim=["Все одноразрядные ошибки исправлены", # Примечания
      "Ни одной 2-х разрядной ошибки не исправлено",
      "Ни одной 3-х разрядной ошибки не исправлено",
      "Ни одной 4-х разрядной ошибки не исправлено",
      "Ни одной 5-ти разрядной ошибки не исправлено",
      "Ни одной 6-ти разрядной ошибки не исправлено",
	"7-ми разрядная ошибка не исправлена"]
print("Выполнил: студент Гусев С.Р., группа ИУ5Ц-72, вариант 26")
print("Информационный вектор:")
print_bin(inform_vector) #Выводим данный вектор
# Кодирование: пункт 1 - сдвиг
inform_vector<<=3 #Сдвигаем информационный вектор
print("Сдвинутый информационный вектор:")
print_bin(inform_vector)
# Кодирование: пункт 2 - деление
rest=(division(inform_vector, p_polinom))
# Кодирование: пункт 3 - конкатенация
cycle_cod=inform_vector^rest # Циклический код Ц[7,4]
print("Циклический код:")
print_bin(cycle_cod)
print("")
for error_vector in range(127):
    r_x=cycle_cod^error_vector # r_x - принятый вектор
    rest_r_x=division(r_x, p_polinom) # Cиндром
    if str(bin(rest_r_x)).count("1") == 0: continue #Если синдром - 0, то считаем что нет ошибки
    find_error=0b1 # Ищем ошибку
    while True :
        rest_error=division(find_error, p_polinom)
        if rest_error == rest_r_x: break #Нашли ошибку
        else: find_error*=2
    if (r_x^find_error==cycle_cod): # Правильно ли нашли ошибку
        fixed_errors[str(bin(error_vector)).count("1")-1]+=1 #Если правильно - инкремент счетчика
#Вывод таблицы
print('┌───┬─────┬────┬────┬─────────────────────────────────────────────┐')
print("%1s%3s%1s%5s%1s%4s%1s%4s%1s%45s%1s" % ("│",'i ',"│","C^i_n","│","N_k","│","C_k","│","Примечание","│"))
for i in range(7):
    C_i_n=math.factorial(7)/(math.factorial(i+1)*math.factorial(6-i))
    print('├───┼─────┼────┼────┼─────────────────────────────────────────────┤')
    print("%1s%3d%1s%5s%1s%4s%1s%4s%1s%45s%1s" % ("│", i + 1, "│", int(C_i_n), "│", fixed_errors[i], "│", int(fixed_errors[i] / C_i_n), "│", prim[i], "│"))
print('└───┴─────┴────┴────┴─────────────────────────────────────────────┘')
