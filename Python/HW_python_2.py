# Python. Homework_2
import random
#1) Создать 2 переменных типа String с разными значениями
S1 = 'Hello'
S2 = "World"
#2) Создать 4 переменных типа Integer с разными значениями
First = 1
Two = 24
Three = 576
Four = 13
#3) Создать 3 переменных типа Float с разными значениями
Fone = 0.24
Ftwo = 57.6
FThree = 13

#4) Реализовать 15 вариантoв сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
A = 1
B = 13
C = -24
Zero = 0
if(B > A):
    print("The variable", B, "is larger than", A)
if(B >= A):
    print("The variable", B, "is larger than or equal to", A)
if(A < B):
    print("The variable", A, "is less than", B)
if(A <= B):
    print("The variable", A, "is less than or equal to", B)
if(B != A):
    print("The variable", B, "is not equal to", A)
if(A*A < B):
    print("The variable", A*A, "is less than", B)
if(B >= A*B):
    print("The variable", B, "is larger than or equal to", A*B)
if((A+B-C) < B):
    print("The variable", (A+B-C), "is larger than", B)
if((A-C) >= B):
    print("The variable", (A-C), "is larger than or equal to", B)
if(B**B != A):
    print("The variable", B**B, "is not equal to", A)
if(B > Zero):
    print("The variable", B, "is positive")
if(C < Zero):
    print("The variable", C, "is negative")
if(C*C > Zero):
    print("The variable", C*C, "is positive")
if(C**B < Zero):
    print("The variable", C**B, "is negative")
if((2*B+C-2*A) == 0):
    print("The variable", (2*B+C-2*A), "is equal to zero")
A =9
B =-5
C =-4

if((A+B+C) == 0):
    print("The variables are the coefficients of a quadratic equation ")

#5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
FA = 1.0
FB = 13.13
FC = -24.576
FZ = 0.0

if(FB > FA):
    print("The variable", FB, "is larger than", FA)
if(FB >= FA):
    print("The variable", FB, "is larger than or equal to", FA)
if(FA < FB):
    print("The variable", FA, "is less than", FB)
if(FA <= FB):
    print("The variable", FA, "is less than or equal to", FB)
if(FB != FA):
    print("The variable", FB, "is not equal to", FA)
if(FA*FA < FB):
    print("The variable", FA*FA, "is less than", FB)
if(FB >= FA*FB):
    print("The variable", FB, "is larger than or equal to", FA*FB)
if((FA+FB-FC) < FB):
    print("The variable", (FA+FB-FC), "is larger than", FB)
if((FA-FC) >= FB):
    print("The variable", (FA-FC), "is larger than or equal to", FB)
#6) Реализовать 10 вариантoв сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты вывести в консоль.
A = 1
B = 13
C = -24

if((B > A) or (B < A)):
    print("1The variable", B, "is larger than", A);
if((C*C >B) and not(B <= A)):
    print("2The variable", B, "is larger than or equal to", A)
if(not(B < A)):
    print("3The variable", A, "is less than", B)
if(not(A >= B)):
    print("4The variable", A, "is less than or equal to", B)
if(not(B == A)):
    print("5The variable", B, "is not equal to", A)
if((A*A < B) or (C >B)):
    print("6The variable", A*A, "is less than", B)
if((B <= A*B) and (B >= C*B)):
    print("7The variable", B, "is larger than or equal to", A*B)
if(not(not(not((A+B-C) < B)))):
    print("8The variable", (A+B-C), "is larger than", B)
if((A-C) >= B or (A-A==-1)):
    print("9The variable", (A-C), "is larger than or equal to", B)
if(not(B**B == A)):
    print("10The variable", B**B, "is not equal to", A)

#7) Сделать скрипт используя функцию input().
    #1. Функция должна на вход принимать целое число.
    #2. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) 30"


    def Digit(Entr):
        print("Вы ввели число =", Entr, end=' ')
        if (Entr < 30):
            print("которое меньше 30")
        elif (Entr > 30):
            print("которое больше 30")
        else:
            print("которое равно 30")

    Enter = int(input("Введите целое число: "))
    Digit(Enter)
#😍 Сделать скрипт используя функцию input().
    #1. Функция должна на вход принимать целое число.
    #2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
    #3. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"

    def Rand_digit(Entr):
        DRand = random.randint(1,100)
        print("Вы ввели число =", Entr, end=' ')
        if (Entr < DRand):
            print("которое меньше", DRand)
        elif (Entr > DRand):
            print("которое больше",DRand)
        else:
            print("которое равно", DRand)

    Enter = int(input("Введите целое число: "))
    Rand_digit(Enter)
#9) Сделать скрипт используя функцию input().
    #1. Функция должна на вход принимать целое число.
    #2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
    #3. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
    def Rand_digit2(Entr):
        DRand1 = random.randint(1,100)
        DRand2 = random.randint(1, 100)
        print("Вы ввели число =", Entr, end=' ')
        if (Entr < DRand1):
            print("которое меньше", DRand1, end=' ')
            if (Entr < DRand2):
                print("и меньше", DRand2)
            elif (Entr > DRand2):
                print("и больше", DRand2)
            else:
                print("и равно", DRand2)
        elif (Entr > DRand1):
            print("которое больше",DRand1)
            if (Entr < DRand2):
                print("и меньше", DRand2)
            elif (Entr > DRand2):
                print("и больше", DRand2)
            else:
                print("и равно", DRand2)
        else:
            print("которое равно", DRand1)
            if (Entr < DRand2):
                print("и меньше", DRand2)
            elif (Entr > DRand2):
                print("и больше", DRand2)
            else:
                print("и равно", DRand2)

    Enter = int(input("Введите целое число: "))
    Rand_digit2(Enter)