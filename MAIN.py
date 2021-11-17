import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time as tm
def plus():
    print("Вы выбрали 'Сложение', ответ будет дан в десятичной\nУкажите первое число")
    firstnum = int(input())
    print("Укажите систему счисления первого числа")
    firstnumsys = int(input())
    print("Укажите второе число")
    secnum = int(input())
    print("Укажите систему счисления второго числа")
    secnumsys = int(input())
    print(f"Вы хотите сложить число {firstnum} в {firstnumsys} сс с {secnum} в {secnumsys} сс")
    actualans = 0
    # переводим firstnum в 10 сс
    ans = 0
    save1 = firstnum
    save2 = secnum
    for i in range(len(str(firstnum))):
        currentnum = firstnum % 10
        ans = ans + currentnum * firstnumsys ** i
        firstnum = firstnum // 10
        # ans - число firstnum в 10 сс
    actualans = actualans + ans
    for i in range(len(str(secnum))):
        currentnum = secnum % 10
        ans = ans + currentnum * secnumsys ** i
        secnum = secnum // 10
    actualans = actualans + ans // 2
    tm.sleep(1.5)
    print(f"Сумма {save1} в {firstnumsys} сс и {save2} в {secnumsys} сс равна {actualans} в 10 сс\n-------------------------")
    tm.sleep(3)
    invite()


def translate():
    wanttoexit4 = ""
    print("Вы выбрали 'Перевод'\nУкажите систему счисления, в которой находится ваше число изначально")
    beginsys = int(input())
    print("Укажите систему, в которую вы хотите перевести")
    endsys = int(input())
    print("Укажите само число")
    translatenum = int(input())
    print(f"Вы собираетесь перевести число {translatenum} из {beginsys} сс в {endsys}")

    save = translatenum
    if endsys == 10:
        ans = 0
        for i in range(len(str(translatenum))):
            currentnum = translatenum % 10
            ans = ans + currentnum * beginsys ** i
            translatenum = translatenum // 10
        print(f"------------------------- \nЧисло {save} в {beginsys} cc равно числу {ans} в {endsys} сс")
    elif beginsys == 10:
        ansmassive = []
        while translatenum > endsys:
            if translatenum <= endsys:
                break
            ansmassive.append(translatenum % endsys)
            translatenum = translatenum // endsys
        ansmassive.append(translatenum)
        ansmassive.reverse()
        answercycle = ""
        for i in range(len(ansmassive)):
            answercycle = answercycle + str(ansmassive[i])
        print(f"------------------------- \nЧисло {save} в {beginsys} cc равно числу {answercycle} в {endsys} сс\n-------------------------")
    elif beginsys != 10 and endsys != 10:
        ans = 0
        for i in range(len(str(translatenum))):
            currentnum = translatenum % 10
            ans = ans + currentnum * beginsys ** i
            translatenum = translatenum // 10
        #число в 10 равно ans
        ansmassive = []
        while ans > endsys:
            if ans <= endsys:
                break
            ansmassive.append(ans % endsys)
            ans = ans // endsys
        ansmassive.append(ans)
        ansmassive.reverse()
        answercycle = ""
        for i in range(len(ansmassive)):
            answercycle = answercycle + str(ansmassive[i])
        print(
            f"------------------------- \nЧисло {save} в {beginsys} cc равно числу {answercycle} в {endsys} сс\n-------------------------")
    tm.sleep(3.5)

    invite()

def navigationone(x):
    if x == 1:
        translate()
    if x == 2:
        plus()
    else:
        print("Введенного вами вариантиа не существует\n")
        tm.sleep(0.8)
        systemnums()
def systemnums():
    print("Вы выбрали 'Действие со системами счисления'\nЧто именно вы хотите сделать? Укажите соответствующий номер: \n  1.Перевод \n  2.Сложение\nВнимание! Программа корректно работает только с системами ниже одиннадцатиричной! ")
    chooseslideone = int(input())
    navigationone(chooseslideone)

def builddiagramm():
    slidezerochoise = 4
    wanttoexit4 = ""
    while wanttoexit4 != "Да" or wanttoexit4 != "ДА" or wanttoexit4 != 'да':
        if wanttoexit4 == "ДА" or wanttoexit4 == "Да" or wanttoexit4 == 'да':
            break
        diagrammorgraph = 1
        if diagrammorgraph == 1:
            print("Вы выбрали построить круговую диаграмму")
            print("Введите название диаграммы")
            namediagr = input()
            print("Введите в одну строчку наименования секторов в одну строчку")
            diagrammnames = list(map(str, input().split()))
            print("Введите в одну строчку значения секторов\nВводить требуется в том же порядке, что и наименования")
            diagrammvalues = list(map(int, input().split()))
            while len(diagrammnames) != len(diagrammvalues):
                print("Один из ваших наборов данных длиннее другого, введите сначала наименования, а заетм и числа заново")
                diagrammnames = list(map(str, input().split()))
                diagrammvalues = list(map(int, input().split()))
            plt.figure(num=1, figsize=(6, 6))
            plt.axes(aspect=1)
            plt.title(namediagr, size=14)
            plt.pie(diagrammvalues, labels=diagrammnames, shadow=True, autopct='%1.1f%%')
            plt.show()
            tm.sleep(2)
            print("-------------------------\nВы хотите выйти в меню? Для ответа напишите 'Да' или 'Нет' ")
            wanttoexit4 = input()
    invite()


def randomnum():
    slidezerochoise = 4
    wanttoexit4 = ""
    while wanttoexit4 != "Да" or wanttoexit4 != "ДА" or wanttoexit4 != 'да':
        if wanttoexit4 == "ДА" or wanttoexit4 == "Да" or wanttoexit4 == 'да':
            break
        print("Вы выбрали 'Сгенерировать случайное число в диапозоне' \nНапишите в одну строчку два числа: начало диапозона и его конец")
        startrandom, endrandom = map(int, input().split())
        while endrandom < startrandom:
            print("Конец диапозона меньше чем начало, введите числа заново")
            startrandom, endrandom = map(int, input().split())
        print(f"Сгенерированное число в диапозоне от {startrandom} до {endrandom} равно {rand.randint(startrandom, endrandom)}")
        tm.sleep(1)
        print("-------------------------\nВы хотите выйти в меню? Для ответа напишите 'Да' или 'Нет' ")
        wanttoexit4 = input()
    invite()


def navigation(chosenslide):
    if chosenslide == 3:
        randomnum()
    elif chosenslide == 2:
        builddiagramm()
    elif chosenslide == 1:
        systemnums()
    else:
        print("Введенного вами варианта не существует\n")
        tm.sleep(0.8)
        invite()

def invite():
    global currentslide
    currentslide = 0
    # создадим переменную, которая будет контролировать текущий слайд
    print(
        "Выберите одну из доступных функций: \n1. Действия со системами счисления \n2. Посторить круговую диаграмму \n3. Сгенерировать случайное число в диапозоне")
    print("------------------------- \nУкажите цифру желаемого варианта")
    slidezerochoise = int(input())
    navigation(slidezerochoise)

#короче готово, я задрался уже, буду просто контент резать (30.20.2021)
invite()