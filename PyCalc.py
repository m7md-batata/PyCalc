import tkinter as tk



calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)



def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)  # corrected from 'result' to 'calculation'
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""  # Clear the calculation string
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("355x300")
#putting a title
root.title("PyCalc")


text_result = tk.Text(root, height=2,width=20, font=("Ubuntu", 24))
text_result.grid(columnspan=5)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Ubuntu", 14))
btn_1.grid(row=2, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Ubuntu", 14))
btn_2.grid(row=2, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Ubuntu", 14))
btn_3.grid(row=2, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Ubuntu", 14))
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Ubuntu", 14))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Ubuntu", 14))
btn_6.grid(row=3, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Ubuntu", 14))
btn_7.grid(row=4, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Ubuntu", 14))
btn_8.grid(row=4, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Ubuntu", 14))
btn_9.grid(row=4, column=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Ubuntu", 14))
btn_0.grid(row=5, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Ubuntu", 14))
btn_plus.grid(row=5, column=0)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Ubuntu", 14))
btn_minus.grid(row=5, column=2)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Ubuntu", 14))
btn_multiply.grid(row=6, column=0)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Ubuntu", 14))
btn_divide.grid(row=6, column=1)
btn_percent = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Ubuntu", 14))
btn_percent.grid(row=6, column=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Ubuntu", 14))
btn_equals.grid(row=6, column=3)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Ubuntu", 14))
btn_open.grid(row=5, column=3)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Ubuntu", 14))
btn_close.grid(row=4, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Ubuntu", 14))
btn_clear.grid(row=6, column=2)
btn_point = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Ubuntu", 14))
btn_point.grid(row=3, column=3)


root.bind("1", lambda event: add_to_calculation(1))
root.bind("2", lambda event: add_to_calculation(2))
root.bind("3", lambda event: add_to_calculation(3))
root.bind("4", lambda event: add_to_calculation(4))
root.bind("5", lambda event: add_to_calculation(5))
root.bind("6", lambda event: add_to_calculation(6))
root.bind("7", lambda event: add_to_calculation(7))
root.bind("8", lambda event: add_to_calculation(8))
root.bind("9", lambda event: add_to_calculation(9))
root.bind("0", lambda event: add_to_calculation(0))
root.bind(".", lambda event: add_to_calculation("."))
root.mainloop()
