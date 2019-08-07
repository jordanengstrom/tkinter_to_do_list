import tkinter as tk
from tkinter import Frame
from tkinter import OptionMenu
from tkinter import StringVar

class AddBox(tk.Frame):

    # high = {'p_type': 'high',
    #         'p_level': 2}
    # medium = {'p_type': 'medium',
    #         'p_level': 1}
    # low = {'p_type': 'low',
    #         'p_level': 0}
    # priorities = [high, medium, low]

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.msg_top = 'Add task: '
        self.msg_drop_down = 'priority: '
        self.text = tk.Text(self, *args, **kwargs)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.tkvar = StringVar(self, parent).set('low')
        self.choices = {'low', 'medium', 'high'}
        self.opt_menu = OptionMenu(mainframe, self.tkvar, self.choices)
        self.opt_menu.grid(row=0, column=0)

root = tk.Tk()
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky='NWES')
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# tkvar = StringVar(root)
# choices = {'low', 'medium', 'high'}
# tkvar.set('low')

# opt_menu = OptionMenu(mainframe, tkvar, *choices)
opt_menu.grid(row=0, column=0)

# Goal: reduce to AddBox(root)

root.mainloop()