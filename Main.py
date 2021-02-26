from tkinter import *

window = Tk()
window.title('Permutation & Combination Calculator')
window.geometry('500x200')
window.resizable(width=False, height=False)

n = Entry(window, font='arial 13 bold')
r = Entry(window, font='arial 13 bold')
filler = Label(window, text='   ')
n.grid(row=0, column=1)
filler.grid(row=1, column=1)
r.grid(row=2, column=1)

def is_valid(str):
    if(str[0]=='0'):
        return False
    for char in range(len(str)):
        if ord(str[char])<48 or ord(str[char])>57:
            return False
    return True

def remove(row, col):
    text = '                          '
    lb = Label(window, text=text, font='arial 13 bold')
    lb.grid(row=row, column=col)

def factorial(number):
    if number <=1:
        return 1
    else:
        fact = 1
        for n in range(2,number+1):
            fact *= n
        return fact

def nPr(n, r):
    return factorial(n) / factorial(n-r)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def permutation():
    n_val = n.get()
    r_val = r.get()
    if is_valid(n_val) and is_valid(r_val):
        n_val = int(n_val)
        r_val = int(r_val)
        if n_val>=r_val:
            perm = nPr(n_val, r_val)
            perm = int(perm)
            remove(4, 1)
            text = str(perm)
            lb = Label(window, text=text, font='arial 13 bold')
            lb.grid(row=4, column=1)
        else:
            remove(4, 1)
            text = 'invalid input!'
            lb = Label(window, text=text, font='arial 13 bold')
            lb.grid(row=4, column=1)
    else:
        remove(4, 1)
        text = 'invalid input!'
        lb = Label(window, text=text, font='arial 13 bold')
        lb.grid(row=4, column=1)

def combination():
    n_val = n.get()
    r_val = r.get()
    if is_valid(n_val) and is_valid(r_val):
        n_val = int(n_val)
        r_val = int(r_val)
        if n_val>=r_val:
            comb = nCr(n_val, r_val)
            comb = int(comb)
            remove(6, 1)
            text = str(comb)
            lb = Label(window, text=text, font='arial 13 bold')
            lb.grid(row=6, column=1)
        else:
            remove(6, 1)
            text = 'invalid input!'
            lb = Label(window, text=text, font='arial 13 bold')
            lb.grid(row=6, column=1)
    else:
        remove(6, 1)
        text = 'invalid input!'
        lb = Label(window, text=text, font='arial 13 bold')
        lb.grid(row=6, column=1)


n_label = Label(window, text='Value of n', font='arial 13 bold')
r_label = Label(window, text='Value of r', font='arial 13 bold')
filler_1 = Label(window, text='   ')

n_label.grid(row=0, column=0)
filler_1.grid(row=1,column=0)
r_label.grid(row=2, column=0)

filler_3 = Label(window, text='   ')
filler_3.grid(row=3, column=0)

permutation = Button(window, text='Permutation', font='arial 13 bold', command=permutation)
permutation.grid(row=4, column=0)

filler_2 = Label(window, text='   ')
filler_2.grid(row=5, column=0)

combination = Button(window, text='Combination', font='arial 13 bold', command=combination)
combination.grid(row=6, column=0)

window.mainloop()


