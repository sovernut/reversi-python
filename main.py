print("reversi")
array = []
row = []
turn =' o'

for i in range(0,8):
    row = []
    for j in range(0,8):
        row.append(str(i)+str(j))
    array.append(row)
 
def printBoard(): 
    for i in range(0,8):
        for j in range(0,8):
            if(j == 7):
                print(array[i][j]+' ')
            else:  
                print(array[i][j]+' ', end='')  

printBoard()
while True:
    pos = input("Enter position: ")
    if len(pos)==2:
        row = int(pos[0])
        col = int(pos[1])
        if row > 7 or col > 7 or row < 0 or col < 0:
            break
        array[row][col] = turn
        printBoard()
    else:
        break