# functions to solve NFA to DFA
import tkinter
import datetime
# make a gui
m = tkinter.Tk()
m.title('NFA -> DFA')
m.geometry('300x300')

#global vars
accepted_move = ""
output_moves = []
#funtions

def inputfilewrite(states, letters,start,accept,moves):
    filewrite = open('input.txt', 'w')
    filewrite.write(str(states) + '\n')
    filewrite.write(str(letters) + '\n')
    filewrite.write(str(start) + '\n')
    filewrite.write(str(accept) + '\n')
    filewrite.write(str(moves) + '\n')
    filewrite.close()

def accepts(i,m,states,letter):
    for x in m:
        y = 1
        while True:
            str = i + " " + letter + " " + y
            if str == m[x]:
                accepted_move = str
                return True
            else:
                y = y + 1
            if y == len(states):
                break
    return False



def run(start, states, moves, accept, letters):
    inputfilewrite(states, letters,start,accept,moves)
    
    #fileread = open('input.txt', 'r')
    x = datetime.datetime.now()
    outf = x.strftime('%H%d') + ".txt"
    if (open(outf, 'r')):
        fileout = open(outf, 'w')
    else:
        fileout = open(outf, 'x')

    i = start # starting state
    move = str(moves).split(', ')
    for i in range(len(str(states))):
        for let in range(len(str(letters))):
            if (accepts(i,move,states,letters[let])):
                output_moves[i] = accepted_move
            else:
                output_moves[i] = str(i) + " " + letters[let] + " " + str(i)
    prntNFA()

def prntNFA():
    for x in output_moves:
        print(x)


    

    









# widgets
# input
tkinter.Label(m, text='States:').grid(row=0, column=0)
states = tkinter.Entry(m)
states.grid(row=0, column=1, columnspan=3)

tkinter.Label(m, text='Letters:').grid(row=1, column=0)
letters = tkinter.Entry(m)
letters.grid(row=1, column=1, columnspan=3)

tkinter.Label(m, text='Start:').grid(row=3, column=0)
start = tkinter.Entry(m)
start.grid(row=3, column=1, columnspan=3)

tkinter.Label(m, text='Accept:').grid(row=4, column=0)
accept = tkinter.Entry(m)
accept.grid(row=4, column=1, columnspan=3)

tkinter.Label(m, text='Moves:').grid(row=5, column=0)
moves = tkinter.Entry(m)
moves.grid(row=5, column=1, columnspan=3)

# button
button = tkinter.Button(m, text='Submit', width=15, command=run(start,states,moves,accept,letters).grid(row=6, column=1))

#output
outputVar = tkinter.Message(m, text = prntNFA).grid(row=7, column= 1)

# run the gui
m.mainloop()
