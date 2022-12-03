# 1 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

#listOfHexNumbers = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
#number = int(input("Введите десятичное число\n"))
#result = []
#while number > 0:
#    result.insert(0, listOfHexNumbers.get(int(number % 16)))
#    number //= 16
#result = [str(i) for i in result]
#print("".join(result))

 # 2 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

#number = float(input("Введите число\n"))
#if number % 1:
#    print("YES")
#else:
#    print("NO")

# 3 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

#value = str(input("Введите строку\n").lower())

#if value.find("о") != -1:
#    value = value[value.index("о") + 1:]
#    if value.find("о") != -1:
#        value = value[:value.rindex("о")]
#        value = value[::-1]
#        print(value)
#    else:
#        print("В строке только один символ 'о'")
#else:
#    print("В строке нет символа 'о'")