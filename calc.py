import tkinter as tk


def get_values():
    num1 = int(number_entry1.get())
    num2 = int(number_entry2.get())
    return num1, num2


def insert_values(value):
    answer_num.delete(0, 'end')
    answer_num.insert(0, value)


def add():
    num1, num2 = get_values()
    rez = num1 + num2
    insert_values(rez)


def sub():
    num1, num2 = get_values()
    rez = num1 - num2
    insert_values(rez)


def div():
    num1, num2 = get_values()
    rez = num1 / num2
    insert_values(rez)


def mil():
    num1, num2 = get_values()
    rez = num1 * num2
    insert_values(rez)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=4, height=2, command=add)
button_add.place(x=75, y=175)
button_sub = tk.Button(window, text='-', width=4, height=2, command=sub)
button_sub.place(x=125, y=175)
button_div = tk.Button(window, text='/', width=4, height=2, command=div)
button_div.place(x=175, y=175)
button_mul = tk.Button(window, text='*', width=4, height=2, command=mil)
button_mul.place(x=225, y=175)
number_entry1 = tk.Entry(window, width=30)
number_1 = tk.Label(window, text='Введите первое число:')
number_1.place(x=75, y=50)
number_entry1.place(x=75, y=75)
number_entry2 = tk.Entry(window, width=30)
number_2 = tk.Label(window, text='Введите второе число:')
number_2.place(x=75, y=100)
number_entry2.place(x=75, y=125)
answer_num = tk.Entry(window, width=30)
answer_num.place(x=75, y=270)
answer_lab = tk.Label(window, text='Ответ:')
answer_lab.place(x=75, y=245)
window.mainloop()
