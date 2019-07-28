#!/usr/bin/python3

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title('Hello World')

        tk.Label(self, text='This is your first GUI! Highfive!').pack()
        tk.Button(self, text='OK', default='active',
                  command=self.click_ok).pack(side='right')
        tk.Button(self, text='Cancel',
                  command=self.click_cancel).pack(side='right')


    def click_ok(self):
        print("The user clicked 'OK'")


    def click_cancel(self):
        print("The user clicked 'Cancel'")
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    app = App(root)
    app.mainloop()

    menubar = tk.Menu(root)
