bornyear=''
birthday=''
while bornyear!=1799:
    bornyear = input('Введите цифрами год рождения А.С.Пушкина')
    while not bornyear.isdigit():
        bornyear = input('Введите цифрами год рождения А.С.Пушкина')
    bornyear=int(bornyear)
    if bornyear==1799:
        print('Год введен верно')
        while birthday!=6.06:
            month=''
            day=''
            while not month.isdigit():
                month = input('Введите цифрами месяц рождения А.С.Пушкина')
            while not day.isdigit():
                day = input('Введите цифрами день рождения А.С.Пушкина')
            birthday = day + '.' + month
            birthday = float(birthday)
            if birthday == 6.06:
                print('Верно')
                break
            else:
                print('Вы ошиблись, попробуйте снова')
    else: print('Вы ошиблись, введите снова')