# functions to solve NFA to DFA
import tkinter

# make a gui
m = tkinter.Tk()
m.title('NFA -> DFA')
m.geometry('300x300')

#funtions


#
# Not my code with be rewritting to use array instead of json
# https://github.com/narenakash/NFA-to-DFA-Converter
#
import json
from collections import OrderedDict

def withjson():
    with open('input.json') as input_file:
        data = json.load(input_file)

    dfa_st = 2 ** data["states"]
    dfa_le = data['letters']
    dfa_sr = data['start']
    dfa_t = [] 
    dfa_fin = []
    #dfa_li = []
    q = []

    q.append((dfa_sr,))

    nfa_trans = {}
    dfa_trans = {}

    for transition in data['t_func']:
        nfa_trans[(transition[0],transition[1])] = transition[2]

    for in_state in q:
        for symbol in dfa_le:
            if len(in_state) == 1 and (in_state[0], symbol) in nfa_trans:
                dfa_trans[(in_state, symbol)] = nfa_trans[(in_state[0], symbol)]

                if tuple(dfa_trans[(in_state,symbol)]) not in q:
                    q.append(tuple(dfa_trans[(in_state, symbol)]))
            else:
                dest = []
                f_dest = []

                for n_state in in_state:
                    if (n_state,symbol) in nfa_trans and nfa_trans[(n_state, symbol)] not in dest:
                        dest.append(nfa_trans[(n_state, symbol)])
            
                if dest:
                    for d in dest:
                        for value in d:
                            if value not in f_dest:
                                f_dest.append(nfa_trans[(n_state, symbol)])
    
                    dfa_trans[(in_state, symbol)] = f_dest

                    if tuple(f_dest) not in q:
                        q.append(tuple(f_dest))

    for key, value in dfa_trans.items():
        temp_list = [[key[0],key[1], value]]
        dfa_t.extend(temp_list)

    for q_state in q:
        for f_state in data["final"]:
            if f_state in q_state:
                dfa_fin.append(q_state)


    dfa = OrderedDict()
    dfa["states"] = dfa_st
    dfa["letters"] = dfa_le
    dfa["t_func"] = dfa_t
    dfa["start"] = dfa_sr
    dfa["final"] = dfa_fin

    output_file = open('output.json', 'w+')
    json.dump(dfa,output_file,separators=(',/t',':'))
    output_file.close()
    input_file.close()

# widgets
# input
tkinter.Label(m, text='States:').grid(row=0, column=0)
eq = tkinter.Entry(m)
eq.grid(row=0, column=1, columnspan=3)

tkinter.Label(m, text='Letters:').grid(row=1, column=0)
es = tkinter.Entry(m)
es.grid(row=1, column=1, columnspan=3)

tkinter.Label(m, text='t_func:').grid(row=2, column=0)
ef = tkinter.Entry(m)
ef.grid(row=2, column=1, columnspan=3)

tkinter.Label(m, text='Start:').grid(row=3, column=0)
est = tkinter.Entry(m)
est.grid(row=3, column=1, columnspan=3)

tkinter.Label(m, text='Final:').grid(row=4, column=0)
eff = tkinter.Entry(m)
eff.grid(row=4, column=1, columnspan=3)
# button
button = tkinter.Button(m, text='Submit', width=15, command=withjson).grid(row=5, column=1)

#output
outputVar = tkinter.Message(m, text = 'output').grid(row=6, column= 1)

# run the gui
m.mainloop()
