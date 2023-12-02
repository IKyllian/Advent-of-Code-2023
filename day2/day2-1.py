f = open("inputs2-1.txt", "r")
lines = f.readlines()
colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}
def game_check(sets):
 for gameSet in sets:
        datas = gameSet.split(',')
        for data in datas:
            data = data.strip().split(' ')
            if int(data[0]) > colors[data[1]]:
                return False
 return True

summ = 0
for line in lines:
    # Separate game ids from content
    parse = line.split(':')
    # Get gameId
    gameId = parse[0].split(' ')[1]
    # Separate all game sets
    sets = parse[1].split(';')
    # Check if the game is valid
    if game_check(sets) == True:
        summ += int(gameId)
   
print(summ)