# functions to solve NFA to DFA
import tkinter
import datetime
# make a gui
m = tkinter.Tk()
m.title('NFA -> DFA')
m.geometry('300x300')

#global vars
accepted_move = ""

#funtions
def inputfilewrite(eq,es,est,eff,moves):
    filewrite = open('input.txt', 'w')
    filewrite.write(eq + '\n')
    filewrite.write(es + '\n')
    filewrite.write(est + '\n')
    filewrite.write(eff + '\n')
    filewrite.write(moves + '\n')
    filewrite.close()

def acceptsA(i,m,states):
    for x in m:
        y = 1
        while True:
            str = i + " a " + y
            if str == m[x]:
                accepted_move = str
                return True
            else:
                y = y + 1
            if y == len(states):
                break
    return False

def acceptsB(i,m,states):
    for x in m:
        y = 1
        while True:
            str = i + " b " + y
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
    output_moves = []
    #fileread = open('input.txt', 'r')
    x = datetime.datetime.now()
    outf = x.strftime('%H%d') + ".txt"
    fileout = open(outf, 'x')

    i = start # starting state
    move = moves.split(', ')
    for i in states:
        if (acceptsA(i,move,states)):
            output_moves[i] = accepted_move
        else:
            output_moves[i] = i + ' a ' + i
        if (acceptsB(i,move,states)):
            output_moves[i] = accepted_move
        else:
            output_moves[i] = i + ' b ' + i

def prntmvs():
    

    









# widgets
# input
tkinter.Label(m, text='States:').grid(row=0, column=0)
eq = tkinter.Entry(m)
eq.grid(row=0, column=1, columnspan=3)

tkinter.Label(m, text='Letters:').grid(row=1, column=0)
es = tkinter.Entry(m)
es.grid(row=1, column=1, columnspan=3)

tkinter.Label(m, text='Start:').grid(row=3, column=0)
est = tkinter.Entry(m)
est.grid(row=3, column=1, columnspan=3)

tkinter.Label(m, text='Accept:').grid(row=4, column=0)
eff = tkinter.Entry(m)
eff.grid(row=4, column=1, columnspan=3)

tkinter.Label(m, text='Moves:').grid(row=5, column=0)
moves = tkinter.Entry(m)
moves.grid(row=5, column=1, columnspan=3)

# button
button = tkinter.Button(m, text='Submit', width=15, command=run(est,eq,moves,eff,es)).grid(row=6, column=1)

#output
outputVar = tkinter.Message(m, text = prntmvs).grid(row=7, column= 1)

# run the gui
m.mainloop()
