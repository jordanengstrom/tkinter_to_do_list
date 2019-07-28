#!/usr/bin/python3
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox


# =============================  functions  =============================
def add_task(*args):
    global tasks
    task = txt_input.get()
    if task is not '':
        tasks.append(task)
    else:
        lbl_display['text'] = 'Please enter a task.'
    txt_input.delete(0, 'end')
    update_listbox()


def del_all():
    # Since we are changing the list, it needs to be global
    global tasks
    if len(tasks) == 0:
        lbl_display['text'] = 'Your list is already empty.'
    else:
        confirmed = messagebox.askyesno('Confirm: Delete All',
                                        'Do you really want to delete all?')
        if confirmed:
            # Clear the tasks list
            tasks = []
            update_listbox()
            show_number_of_tasks()


def del_one():
    # Get the text of the currently selected item
    task = lb_tasks.get('active')
    # Confirm it's in the list
    if task in tasks:
        tasks.remove(task)
        update_listbox()
    else:
        lbl_display['text'] = 'You must first select a task to delete it.'


def sort_asc():
    if len(tasks) == 0:
        lbl_display['text'] = 'No tasks to sort. Please add tasks, then sort.'
    else:
        tasks.sort()
        update_listbox()


def sort_dsc():
    if len(tasks) == 0:
        lbl_display['text'] = 'No tasks to sort. Please add tasks, then sort.'
    else:
        tasks.sort()
        tasks.reverse()
        update_listbox()


def choose_random():
    if len(tasks) == 0:
        lbl_display['text'] = 'No tasks to choose from.'
    else:
        task = random.choice(tasks)
        lbl_display['text'] = task


def show_number_of_tasks():
    # Get the number of tasks
    number_of_tasks = len(tasks)
    # Display the message
    lbl_display['text'] = 'Number of tasks: %s' % number_of_tasks


# Populates the listbox in the window
def update_listbox():
    # Clear the current list
    clear_listbox()
    # Repopulate the current list
    for t in tasks:
        lb_tasks.insert('end', t)


def clear_listbox():
    # Clear the tasks indexed from 0 to 'end'
    lb_tasks.delete(0, 'end')


def do_nothing():
    lbl_display['text'] = 'do_nothing was called'
    pass


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

# Create root window
root = tk.Tk()
if get_platform() == 'OS X':
    app_ico = tk.Image('photo', file='./images/png_files/main_icon.png')
    root.iconphoto(True, app_ico)
    root.wm_iconbitmap(r'./images/icns_files/main_icon.icns')
elif get_platform() == 'Windows':
    print('sucks to suck')

text = Text(root)
text.config(wrap=CHAR)
root.bind('<Return>', add_task)
root.geometry('425x375')
root.title('Jordan\'s To Do List')

menu = Menu(root)
root.config(menu=menu, bg='#ffffff')
sub_menu_1 = tk.Menu(menu)
menu.add_cascade(label='File', menu=sub_menu_1)
sub_menu_1.add_command(label='New', command=add_task)
sub_menu_1.add_command(label='Edit', command=do_nothing)
sub_menu_1.add_separator()
sub_menu_1.add_command(label='Exit', command=exit)
# root.configure(bg='#ffffff')

# tkinter only supports .ico files (and not
# Keep track of data using a list
tasks = []
# For testing purposes use a default list
# tasks = ['play with Benny', 'call Birdy', 'water plants']

lbl_title = tk.Label(root, text='to-do-list', bg='#bee6e2')
lbl_title.grid(row=0, column=0, columnspan=2, sticky='WE')

lbl_display = tk.Label(root, text='', bg='#ffffff', wraplength=155, justify=CENTER)
lbl_display.grid(row=10, column=1, columnspan=1, rowspan=1, sticky='WE')

status_display = tk.Label(root, text='Status:', bg='#ffffff', justify=LEFT)
status_display.grid(row=10, column=0, columnspan=1, rowspan=1, sticky='WE')

txt_input = tk.Entry(root, width=15, text='to-do-list', bg='#ffffff')
txt_input.grid(row=2, column=1, sticky='WE')

lb_tasks = tk.Listbox(root)
lb_tasks.grid(row=3, column=1, rowspan=6)

btn_add_task = tk.Button(root, text='Add Task', fg='#4a6361',
                         command=add_task)
btn_add_task.grid(row=2, column=0, sticky='WE')

btn_del_all = tk.Button(root, text='Delete All', fg='#4a6361',
                        command=del_all)
btn_del_all.grid(row=3, column=0, sticky='WE')

btn_del_one = tk.Button(root, text='Delete', fg='#4a6361', command=del_one)
btn_del_one.grid(row=4, column=0, sticky='WE')

btn_sort_asc = tk.Button(root, text='Sort Asc', fg='#4a6361',
                         command=sort_asc)
btn_sort_asc.grid(row=5, column=0, sticky='WE')

btn_sort_dsc = tk.Button(root, text='Sort Dsc', fg='#4a6361',
                         command=sort_dsc)
btn_sort_dsc.grid(row=6, column=0, sticky='WE')

btn_choose_random = tk.Button(root, text='Choose Random', fg='#4a6361',
                              command=choose_random)
btn_choose_random.grid(row=7, column=0, sticky='WE')

btn_show_number_of_tasks = tk.Button(root, text='Number of Tasks',
                                     fg='#4a6361',
                                     command=show_number_of_tasks)
btn_show_number_of_tasks.grid(row=8, column=0)

btn_exit = tk.Button(root, text='Exit', fg='#4a6361', command=exit)
btn_exit.grid(row=9, column=0, sticky='WE')

# Start the main events loop
root.mainloop()
