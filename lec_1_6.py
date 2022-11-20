# Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
# else:
#    print(b)
# еще есть "elif" - если не выполняеться if, то проверяется по следующим elif


# Управляющие конструкции: while

original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted) # сборка инвертированного числа
print()
print('Дальше по for')
# Управляющие конструкции: for
list = [1,2,3,4,10,5]
for i  in list:
    print(i**2)

r = range(5)
for j in r: # можно сразу писать |for i in range(5)|. Еще можно в range первым аргументом
# указать  с какого элемента начать, а третим шаг range(1, 10, 2) будет показывать все нечетные  
    print(j)
# так же можно использовать со строками( for i in 'qwe - rty')