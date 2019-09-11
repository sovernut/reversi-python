print("reversi")
array = []
row = []

for i in range(0,8):
    row = []
    for j in range(0,8):
        row.append(str(i)+str(j))
    array.append(row)
 
for i in range(0,8):
    for j in range(0,8):
        if(j == 7):
            print(array[i][j]+'')
        else:  
            print(array[i][j]+' ', end = '')  
