bornyear=''
while bornyear!=1799:
    bornyear = input('Введите цифрами год рождения А.С.Пушкина')
    while not bornyear.isdigit():
        bornyear = input('Введите цифрами год рождения А.С.Пушкина')
    bornyear=int(bornyear)
    if bornyear==1799:
        print('Верно')
        break
    else: print('Вы ошиблись')