N = int(input("Введите число N: "))
V = list(map(int, input("Введите числа через пробел: ").split()))
if len(V) != N:
    print("Ошибка: количество введённых чисел не равно N.")
else:
    res = [V[-1]] + [V[0]] + V[1:-1]
print("Изменённый массив:", " ".join(map(str, res)))
