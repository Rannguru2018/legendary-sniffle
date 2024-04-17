import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif symbol == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

# Equation display area
display = tk.Entry(root, width=20, font=('Arial', 16))
display.grid(row=0, column=0, columnspan=4)

# Button symbols
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for button in buttons:
    text, row, col = button
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
                    command=lambda symbol=text: button_click(symbol))
    btn.grid(row=row, column=col)

root.mainloop()
