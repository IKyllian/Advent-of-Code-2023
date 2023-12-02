f = open("inputs2-1.txt", "r")
lines = f.readlines()
def game_check(sets):
 gameColors = {
    'red': 1,
    'green': 1,
    'blue': 1
 }
 for gameSet in sets:
        datas = gameSet.split(',')
        for data in datas:
            data = data.strip().split(' ')
            if (int(data[0]) > gameColors[data[1]]):
                gameColors[data[1]] = int(data[0])
 return int(gameColors['blue'] * gameColors['green'] * gameColors['red'])

summ = 0
for line in lines:
    # Separate game ids from content
    parse = line.split(':')
    # Get gameId
    gameId = parse[0].split(' ')[1]
    # Separate all game sets
    sets = parse[1].split(';')
    summ += game_check(sets) 
   
print(summ)