bornyear=''
day=''
month=''
while not bornyear.isdigit():
    bornyear = input('Введите цифрами год рождения А.С.Пушкина')
bornyear=int(bornyear)
if bornyear==1799:
    while not month.isdigit():
        month = input('Введите цифрами месяц рождения А.С.Пушкина')
    while not day.isdigit():
        day = input('Введите цифрами день рождения А.С.Пушкина')
    birthday=day+'.'+month
    birthday=float(birthday)
    if birthday==6.06:
        print('Верно')
    else: print ('Вы ввели неправильный день')
else: print('Вы ввели неправильный год')