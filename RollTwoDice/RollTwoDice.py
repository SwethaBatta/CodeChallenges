# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:18:14 2020

@author: SwethaBatta
"""

import tkinter
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')
    
# label to display dice
label = tkinter.Label(root, text='', font=('Helvetica', 260))
roll_label = tkinter.Label(root, text='', font=('Helvetica', 25))
    
class RollTwoDice(object):
    
    def __init__(self):
        self.firstDice = {}
        self.secondDice = {}
        self.total = 0
        self.specialCase = ''
        self.dice = [{"val": 1, "img": '\u2680'}, {"val": 2, "img": '\u2681'}, {"val": 3, "img": '\u2682'}, {"val":4, "img": '\u2683'}, {"val":5, "img": '\u2684'}, {"val":6, "img": '\u2685'}]
        self.label = label
        self.roll_label = roll_label


    def computeTotal(self):
        self.total = int(self.firstDice['val'])+int(self.secondDice['val'])
               
    def caseSnakeEyes(self):
        if int(self.firstDice['val']) == int(self.secondDice['val']) == 1:
            self.specialCase = 'Snake Eyes'    
                    
    def caseLucky7(self):
        if self.total == 7:
            self.specialCase = 'Lucky 7' 
    
    def diceValues(self):
        # unicode character strings for dice
        self.firstDice = random.choice(self.dice)
        self.secondDice = random.choice(self.dice)
                
    # function activated by button
    def roll_dice(self):
        self.diceValues()
        self.computeTotal()
        self.caseSnakeEyes()
        self.caseLucky7()
         
        #Dice image display 
        self.label.configure(text=f"{self.firstDice['img']} {self.secondDice['img']}")    
        self.label.pack()
        
        #Score display
        self.roll_label.configure(text=f"First Dice: {self.firstDice['val']} \t Second Dice: {self.secondDice['val']} \n\n Total: {self.total} \n\n {self.specialCase}")    
        self.roll_label.pack()
        
        #Resetting to initial state
        self.specialCase = ''

if __name__ == '__main__':
    rtd = RollTwoDice()
  
    # button
    button = tkinter.Button(root, text='Roll dice', foreground='green', command=rtd.roll_dice)
    # pack a widget in the parent widget
    button.pack()  
    # call the mainloop of Tk
    # keeps window open
    root.mainloop()