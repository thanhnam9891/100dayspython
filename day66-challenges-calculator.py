import tkinter as tk

#variables
expression = ""

def press(num):
    global expression

    expression = expression_field.get()

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression= 0
    except:
        equation.set("error")
        expression=""

def clear():
    global expression
    expression=""
    equation.set("")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator") # Sets the name of the window in the border
    window.geometry("300x150") # Sets the size of the window in pixels

    equation = tk.StringVar()
    expression_field = tk.Entry(window, textvariable=equation)
    expression_field.grid(columnspan=9,ipadx=70)
    

    one_btn = tk.Button(text = "1",command=lambda: press("1"))
    one_btn.grid(row=2,column=0)

    two_btn = tk.Button(text = "2",command=lambda: press("2"))
    two_btn.grid(row=2,column=1)

    three_btn = tk.Button(text = "3",command=lambda: press("3"))
    three_btn.grid(row=2,column=2)

    plus_btn = tk.Button(text = "+",command=lambda: press("+"))
    plus_btn.grid(row=2,column=3)

    minus_btn = tk.Button(text = "-",command=lambda: press("-"))
    minus_btn.grid(row=2,column=4)

    four_btn = tk.Button(text = "4",command=lambda: press("4"))
    four_btn.grid(row=3,column=0)

    five_btn = tk.Button(text = "5",command=lambda: press("5"))
    five_btn.grid(row=3,column=1)

    six_btn = tk.Button(text = "6",command=lambda: press("6"))
    six_btn.grid(row=3,column=2)

    multi_btn = tk.Button(text = "*",command=lambda: press("*"))
    multi_btn.grid(row=3,column=3)

    div_btn = tk.Button(text = "/",command=lambda: press("/"))
    div_btn.grid(row=3,column=4)

    seven_btn = tk.Button(text = "7",command=lambda: press("7"))
    seven_btn.grid(row=4,column=0)

    eight_btn = tk.Button(text = "8",command=lambda: press("8"))
    eight_btn.grid(row=4,column=1)

    nine_btn = tk.Button(text = "9",command=lambda: press("9"))
    nine_btn.grid(row=4,column=2)

    zero_btn = tk.Button(text = "0",command=lambda: press("0"))
    zero_btn.grid(row=5,column=1)

    equal_btn = tk.Button(text = "=", command=equalpress)
    equal_btn.grid(row=5,column=3)

    ac_btn = tk.Button(text = "AC",command=clear)
    ac_btn.grid(row=5,column=4)

    tk.mainloop()

