sum = int(input("Сколько всего сделали журавликов дети? Введите число: "))
a = sum // 6
print(sum, " -> ", "Петя:", a , "Катя: ", a*4 ,"Вова: " , a )
if sum % 6 != 0:
    print("Дети сделали ещё оное(", sum%6, " штуки) ко-во журавликов, но мы ещё не выяснили кто сколько")