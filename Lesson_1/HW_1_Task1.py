a = int(input("Введите 3-х значное число: "))
if 1000 > a >=100:
    s = print(a//100)# просто для красоты вывода. только не поняла, что за 3 пустых значения ?
    u = print(a//10%10)
    m = print(a%10)
    print(s, u, m)
    sum = a//100 + a//10%10 + a%10
    print(sum)
else: print("Вы ввели не 3-х значное число ")