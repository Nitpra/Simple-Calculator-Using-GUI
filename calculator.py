# Python program to create a simple GUI
# How to make a calculator in python using python library tkinter
import tkinter as tk
field_text = ""
def  add_to_field(num):
    global field_text
    field_text =field_text+str(num)
    field.delete('1.0', "end")
    field.insert('1.0', field_text)

def caculate():
        
    global field_texts
    result =str(eval(field_text))
    field.delete('1.0', "end")
    field.insert('1.0', result)

    
        
def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")

# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = tk.Tk()
 
 
    # set the title of GUI window 
    gui.title("Simple Calculator") 
    gui.geometry("400x400")
    field = tk.Text(gui,height=6,width = 28 , font=("Times New Roman", 20))
    field.grid(row=1,column=1,  columnspan=4)


    btn_1 = tk.Button(gui, text="1", command=lambda: add_to_field(1),width=7, font=("Times New Roman", 14))
    btn_1.grid(row=4,column=1)

    btn_2 =  tk.Button(gui, text="2", command=lambda: add_to_field(2),width=7, font=("Times New Roman", 14))
    btn_2.grid(row=4,column=2)

    btn_3 = tk.Button(gui, text="3", command=lambda: add_to_field(3),width=7, font=("Times New Roman", 14))
    btn_3.grid(row=4,column=3)

    btn_4 = tk.Button(gui, text="4", command=lambda: add_to_field(4),width=7, font=("Times New Roman", 14))
    btn_4.grid(row=3,column=1)

    btn_5 = tk.Button(gui, text="5", command=lambda: add_to_field(5),width=7, font=("Times New Roman", 14))
    btn_5.grid(row=3,column=2)

    btn_6 = tk.Button(gui, text="6", command=lambda: add_to_field(7),width=7, font=("Times New Roman", 14))
    btn_6.grid(row=3,column=3)

    btn_7 = tk.Button(gui, text="7", command=lambda: add_to_field(7),width=7, font=("Times New Roman", 14))
    btn_7.grid(row=2,column=1)

    btn_8 = tk.Button(gui, text="8", command=lambda: add_to_field(8),width=7, font=("Times New Roman", 14))
    btn_8.grid(row=2,column=2)

    btn_9 = tk.Button(gui, text="9", command=lambda: add_to_field(9),width=7, font=("Times New Roman", 14))
    btn_9.grid(row=2,column=3)

    btn_0 = tk.Button(gui, text="0", command=lambda: add_to_field(0),width=7, font=("Times New Roman", 14))
    btn_0.grid(row=5,column=1)



# Operation Buttons

    btn_plus = tk.Button(gui, text="+", command=lambda: add_to_field("+"), width=7, font=("Times New Roman", 14))
    btn_plus.grid(row=4, column=4)

    btn_minus = tk.Button(gui, text="-", command=lambda: add_to_field("-"), width=7, font=("Times New Roman", 14))
    btn_minus.grid(row=5, column=4)

    btn_times = tk.Button(gui, text="*", command=lambda: add_to_field("*"), width=7, font=("Times New Roman", 14))
    btn_times.grid(row=3, column=4)

    btn_division = tk.Button(gui, text="/", command=lambda: add_to_field("/"), width=7, font=("Times New Roman", 14))
    btn_division.grid(row=2, column=4)

    btn_clear = tk.Button(gui, text="clear", command=lambda: clear(), width=7, font=("Times New Roman", 14))
    btn_clear.grid(row=5, column=3)

    btn_decimal = tk.Button(gui, text=".", command=lambda: add_to_field(".") , width=7, font=("Times New Roman", 14))
    btn_decimal.grid(row=5, column=2)

    btn_open_parenthesis = tk.Button(gui, text="(", command=lambda: add_to_field("("), width=7, font=("Times New Roman", 14))
    btn_open_parenthesis.grid(row=6, column=1)

    btn_close_parenthesis = tk.Button(gui, text=")", command=lambda: add_to_field(")"), width=7, font=("Times New Roman", 14))
    btn_close_parenthesis.grid(row=6, column=2)

    btn_equal = tk.Button(gui, text="=", command=lambda: caculate(), width=17, font=("Times New Roman", 14))
    btn_equal.grid(row=6, column=3, columnspan=2)

    gui.mainloop()

