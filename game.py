

n= int(input('Количество человек в команде'))
players = {}

for i in range (n):
    name = input('Имя')
    size = input('Размер')
    players[name] = size
    
    if name in players:
        print(players[name])
    else:
        print('Такого человека в команде нет')
    name = input('Введите имя человека')
        
        