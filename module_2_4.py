# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primers_ = []
not_primers = []
for i in numbers_: # пусть i будет numbers_ : (дальше)
    if i > 1:       # если i больше 1 : #
        is_prime = True # переменная is_praime - Правда
        for j in range(2, i):  # пусть j будет исследуемый диапазон (range) списка от (2 до i)
            if (i % j) == 0: # если i делится на j без остатка (%) == 0
                is_prime = False # переменная is_praime - Ложь
                break # при этом вычисление останавливаем
        if is_prime: # если число простое:
            Primers_.append(i) #  то добавляем в список Primes_ ( функция .append)
        else:                   # если нет, то
            not_primers.append(i) #  то добавляем в список not_ primes_ ( функция .append)
print('Primers:', Primers_)
print('Not primers:', not_primers)






