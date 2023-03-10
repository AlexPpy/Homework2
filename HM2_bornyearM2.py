bornyear=''
while not bornyear.isdigit():
    bornyear = input('Введите цифрами год рождения А.С.Пушкина')
bornyear=int(bornyear)
if bornyear==1799:
    print('Верно')
else: print('Вы ошиблись')