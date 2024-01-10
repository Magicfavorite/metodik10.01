import string as str

print(str.digits)

myStr = "python"
print(myStr[4])#четвертый элемент
print(myStr[2:6])#от второго и до шестого
print(myStr[3])#третий символ
print(myStr[:6])#последний символ будет шестой
print(myStr[3:])
print(myStr[:5])
print(myStr[3:6:5])#от трех до шест с шагом в 5 символов
print(myStr[:5:2])
print(myStr[3::2])
print(myStr[::2])
print(myStr[:len(myStr):3])#от начала строки и до конца с шагом в 3 символа
print()
print("\\")
print('\'Python Programming: An Introduction toComputer Science\'')
myStr1="The number1 range from {0:-} to {1:-}"
format(-10)
print(myStr1) #The number1 range from -10 to 10
myStr2="The number2 range from {0:+} to {1:+}"
format(-20)
print(myStr2) #The number2 range from -20 to +50
myStr3="The number3 range from {0: } to {1:}".format(-30,30)
print(myStr3) #The number3 range from -30 to 30
print()


my_List = [3, "three", 17]
print(type(my_List))
sec_list = [13," three"]


list1=[i*i for i in range(6)]
print(list1) #[0, 1, 4, 9, 16, 25]

list2=[i+"*" for i in "example"]
print(list2) #['e*', 'x*', 'a*', 'm*', 'p*', 'l*', 'e*']

list6 = [x*y for x in range(1, 4) for y in range(1, 4)]
print(list6) #[1, 2, 3, 2, 4, 6, 3, 6, 9]

list7 = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(list7) #[[1, 2, 3], [2, 4, 6], [3, 6, 9]]

list4=[i*i for i in range(1,11) if i%2==0]
print(list4) #[4, 16, 36, 64, 100]

print(list1[::2])

for i in list2:
    if i > 10:
        print()

myList = ["user", 12, 200.34, False, True]
print(myList[1])  # 12
print(myList[-1])  # True
print(myList[-2])  # False

myStr="python was created in the late 1980'sby Guido van Rossum."
print(myStr.capitalize()) # Python was created inthe late 1980's by guido van rossum.
print(myStr.lower()) #python was created in the late1980's by guido van rossum.
print(myStr.upper()) #PYTHON WAS CREATED IN THE LATE1980'S BY GUIDO VAN ROSSUM.
print(myStr.title()) #Python Was Created In The Late1980'S By Guido Van Rossum.
print(myStr.swapcase()) #PYTHON WAS CREATED INTHE LATE 1980'S BY gUIDO VAN rOSSUM.