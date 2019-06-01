#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Suivant que l'on exécute ce script sous Python 3 ou Python 2,
# on utilisera le module Tkinter correspondant :
try:
    from tkinter import *      # module Tkinter pour Python 3
except:
    from Tkinter import *      # module Tkinter pour Python 2

fen = Tk()
fen.title("Fenêtre composée à l'aide de frames")
fen.geometry("300x300")

f1 = Frame(fen, bg = '#80c0c0')
f1.pack(side =LEFT, padx =5)  

fint = [0]*6			
for (n, col, rel, txt) in [(0, 'grey50', RAISED, 'Relief sortant'),
                           (1, 'grey60', SUNKEN, 'Relief rentrant'),
                           (2, 'grey70', FLAT, 'Pas de relief'),
                           (3, 'grey80', RIDGE, 'Crête'),
                           (4, 'grey90', GROOVE, 'Sillon'),
                           (5, 'grey100', SOLID, 'Bordure')]:
    fint[n] = Frame(f1, bd =2, relief =rel)
    e = Label(fint[n], text =txt, width =15, bg =col)
    e.pack(side =LEFT, padx =5, pady =5)
    fint[n].pack(side =TOP, padx =10, pady =5)

f2 = Frame(fen, bg ='#d0d0b0', bd =2, relief =GROOVE)
f2.pack(side =RIGHT, padx =5)

can = Canvas(f2, width =80, height =80, bg ='white', bd =2, relief =SOLID)
can.pack(padx =15, pady =15)

bou =Button(f2, text='Bouton')
bou.pack()

fen.mainloop()
