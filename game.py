a = '         '
b = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]
print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
xwins = 1
owins = 1
i = 0
moves = 0
while True:
    d = input('Enter the coordinates:').split()
    if d[0].isnumeric() and d[1].isnumeric():
        k = d[:]
        k[0] = 3 - int(d[1])
        k[1] = int(d[0]) - 1
        if 1 <= int(d[0]) <= 3 and 1 <= int(d[1]) <= 3:
            if b[k[0]][k[1]] == ' ' and i % 2 == 0:
                b[k[0]][k[1]] = 'X'
                print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
                i += 1
                if b[0][2] == b[1][1] == b[2][0] == 'X' or b[1][1] == b[0][0] == b[2][2] == 'X':
                    print('X wins')
                    break
                else:
                    for j in range(3):
                        if b[j][0] == b[j][1] == b[j][2] == 'X' or b[0][j] == b[1][j] == b[2][j] == 'X':
                            print('X wins')
                            break

            elif b[k[0]][k[1]] == ' ' and i % 2 == 1:
                b[k[0]][k[1]] = 'O'
                print(f'''---------
| {b[0][0]} {b[0][1]} {b[0][2]} |
| {b[1][0]} {b[1][1]} {b[1][2]} |
| {b[2][0]} {b[2][1]} {b[2][2]} |
---------''')
                i += 1
                if b[1][1] == b[0][0] == b[2][2] == 'O' or b[0][2] == b[1][1] == b[2][0] == 'O':
                    print('O wins')
                    break
                else:
                    for j in range(3):
                        if b[j][0] == b[j][1] == b[j][2] == 'O' or b[0][j] == b[1][j] == b[2][j] == 'O':
                            print('O wins')
                            break
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
    moves = sum([b[h].count('X') + b[h].count('O') for h in range(3)])
    if moves == 9:
        print(('Draw'))
        break
