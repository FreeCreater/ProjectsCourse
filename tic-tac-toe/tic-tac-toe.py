from tkinter import *
from tkinter.messagebox import showinfo

WIDTH = 300
HEIGHT = 350

window = Tk()
window.title('tic-tac-toe')
window.geometry(f'{WIDTH}x{HEIGHT}')

field = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]
char = 'x'
turn = 1
win_x = 0
win_o = 0

def show_field():
    for row in range(3):
        for column in range(3):
            Button(
                window, text=field[row][column],
                command=lambda x=row, y=column: user_turn(x, y)
                )\
            .place(x=row * 100, y=column * 100 + 50, relwidth=0.33, relheight=0.3)

def user_turn(x, y):
    global turn
    if field[x][y] != '*': return
    if turn % 2 == 0:
        char = 'x'
    else:
        char = 'o'

    field[x][y] = char
    turn += 1

    show_field()
    if check_winer(x, y, char):
        showinfo('Victory', f'{char} wins')

    
def check_winer(row, column, char):
    if field[row][0] == char and field[row][1] == char and field[row][2] == char:
        return True
    if field[0][column] == char and field[1][column] == char and field[2][column] == char:
        return True
    if field[0][0] == char and field[1][1] == char and field[2][2] == char:
        return True
    if field[0][2] == char and field[1][1] == char and field[2][0] == char:
        return True
    return False

show_field()
label_x = Label(window, text=f'x: {win_x}', width=2).place(x=WIDTH//2-60, y=0)
label_y = Label(window, text=f'o: {win_o}', width=2).place(x=WIDTH//2+40, y=0)

btn_reset = Button(window)

window.mainloop()