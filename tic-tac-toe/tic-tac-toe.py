from tkinter import *
from tkinter.messagebox import showinfo

WIDTH = 300
HEIGHT = 350

window = Tk()
window.title('tic-tac-toe')
window.geometry(f'{WIDTH}x{HEIGHT}')



# field = [
#     ['*', '*', '*'],
#     ['*', '*', '*'],
#     ['*', '*', '*']
# ]


turn = 1
win_x = 0
win_o = 0

def user_turn(x, y):
    global turn
    if field[x][y]['text'] != '*': return
    char = 'x' if turn % 2 == 0 else 'o'

    field[x][y]['text'] = char

    if check_winer(x, y, char):
        showinfo('Victory', f'{char} wins')
        add_points()
        restart()
        return
    if turn == 9:
        showinfo('Draw', 'Draw')
        restart()
    turn += 1

    
def check_winer(row, column, char):
    if field[row][0]['text'] == char and field[row][1]['text'] == char and field[row][2]['text'] == char:
        return True
    if field[0][column]['text'] == char and field[1][column]['text'] == char and field[2][column]['text'] == char:
        return True
    if field[0][0]['text'] == char and field[1][1]['text'] == char and field[2][2]['text'] == char:
        return True
    if field[0][2]['text'] == char and field[1][1]['text'] == char and field[2][0]['text'] == char:
        return True
    return False

def restart():
    global turn
    turn = 0
    for row in range(3):
        for column in range(3):
            field[row][column]['text'] = '*'


field = []
for row in range(3):
    field.append([])
    for column in range(3):
        button = Button(text = '*')
        button['command'] = lambda x=row, y=column: user_turn(x, y)
        button.place(x = column*100, y = row*100+30, relwidth=0.33, relheight=0.3)
        field[row].append(button)



label_x = Label(window, text=f'x: {win_x}', width=2)
label_x.place(x=WIDTH//2-60, y=0)
label_o = Label(window, text=f'o: {win_o}', width=2)
label_o.place(x=WIDTH//2+40, y=0)

def add_points():
    global win_x
    global win_o
    if turn % 2 == 0:
        win_x+=1
        label_x['text'] = f'x: {win_x}'
    else:
        win_o+=1
        label_o['text'] = f'o: {win_o}'

btn_reset = Button(window)

window.mainloop()