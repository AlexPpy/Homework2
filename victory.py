Y_Pushkin=1799
Q_Pushkin=''
Y_Lermontov=1814
Q_Lermontov=''
Y_Eiler=1707
Q_Eiler=''
Y_Lomonosov=1711
Q_Lomonosov=''
Y_Einshtein=1879
Q_Einshtein=''
count=0
while count!=5:
    count=0
    Q=''
    while not Q.isdigit():
        Q = input('Введите цифрами год рождения А.С.Пушкина')
    Q=int(Q)
    if Q==Y_Pushkin:
        count+=1
        print('Верно, ваш счет:',count)
    else: print('Неверно, ваш счет:', count)
    Q = ''
    while not Q.isdigit():
        Q = input('Введите цифрами год рождения А.С.Лермонтова')
    Q = int(Q)
    if Q == Y_Lermontov:
        count +=1
        print('Верно, ваш счет:', count)
    else:
        print('Неверно, ваш счет:', count)
    Q = ''
    while not Q.isdigit():
        Q = input('Введите цифрами год рождения Эйлера')
    Q = int(Q)
    if Q == Y_Eiler:
        count +=1
        print('Верно, ваш счет:', count)
    else:
        print('Неверно, ваш счет:', count)
    Q = ''
    while not Q.isdigit():
        Q = input('Введите цифрами год рождения Ломоносова')
    Q = int(Q)
    if Q == Y_Lomonosov:
        count +=1
        print('Верно, ваш счет:', count)
    else:
        print('Неверно, ваш счет:', count)
    Q = ''
    while not Q.isdigit():
        Q = input('Введите цифрами год рождения Эйнштейна')
    Q = int(Q)
    if Q == Y_Einshtein:
        count +=1
        print('Верно, ваш счет:', count)
    else:
        print('Неверно, ваш счет:', count)
    print('Процент правильных ответов', (count/5)*100, '%')
    x=input('Хотите попробовать еще? Ответьте Y или N ')
    if x=='Y':
        count=0
    else:
        print('Ваш результат:', (count/5)*100, '%')
        break