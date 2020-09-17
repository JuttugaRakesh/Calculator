from tkinter import *
from tkinter import ttk

class Personal_Calculator:
    calVal = 0.0

    div= False
    mult = False
    add = False
    subtract = False
    factorial = False
    fib = False

    # The function where the user clicks on number button
    # We need to add the digit until we get a number
    def button_press(self, value):

        # Get the current value in the entry
        entryVal = self.number_entry.get()
        entryVal += value
        # Clear the entry box
        self.number_entry.delete(0, "end")
        # Insert the new value going from left to right
        self.number_entry.insert(0, entryVal)

    def isFloat(self,strVal):
        try:
            float(strVal)
            return True
        except ValueError:
            return False

    # The function where the user clicks on an operation
    def math_button_press(self, value):
        if self.isFloat(str(self.number_entry.get())):
            self.div = False
            self.mult = False
            self.add = False
            self.subtract = False

            self.calcVal = float(self.entryVal.get())

            if(value == "/"):
                print("/ was pressed")
                self.div = True
            elif( value == "*"):
                print("* was pressed")
                self.mult = True
            elif( value == "+"):
                print("+ was pressed")
                self.add = True
            else:
                print("- was pressed")
                self.subtract = True

            self.number_entry.delete(0, "end")

    # Clear everything
    def clear_button_press(self):
        print("Clearing everything")
        self.div = False
        self.mult = False
        self.add = False
        self.subtract = False
        self.calVal = 0.0
        self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if (self.add or self.subtract or self.div or self.mult):
            if self.add:
                solution = self.calcVal + float(self.entryVal.get())
            elif self.subtract:
                solution = self.calcVal - float(self.entryVal.get())
            elif self.mult:
                solution = self.calcVal * float(self.entryVal.get())
            else:
                if (self.entryVal.get()) == '0':
                    solution = "UNDEFINED"
                else:
                    solution = self.calcVal / float(self.entryVal.get())

        print(self.calcVal,"   ", float(self.entryVal.get()),"  ",solution)
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entryVal = StringVar(root, value="")
        root.title("Personal Calculator")
        root.geometry("597x250")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 35", padding=10)

        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entryVal, width=95,justify='center')
        self.number_entry.grid(row=0, columnspan=4)

        self.button7 = ttk.Button(root, text = "7",
                                  command = lambda:self.button_press('7')).grid(row = 1, column = 0)

        self.button8 = ttk.Button(root, text = "8",
                                  command = lambda:self.button_press('8')).grid(row = 1, column = 1)

        self.button9 = ttk.Button(root, text = "9",
                                  command = lambda:self.button_press('9')).grid(row = 1, column = 2)

        self.buttonDiv = ttk.Button(root, text="/",
                                    command=lambda: self.math_button_press('/')).grid(row = 1, column = 3)

        # Start of the second row

        self.button4 = ttk.Button(root, text = "4",
                                  command = lambda:self.button_press('4')).grid(row = 2, column = 0)

        self.button5 = ttk.Button(root, text = "5",
                                  command = lambda:self.button_press('5')).grid(row = 2, column = 1)

        self.button6 = ttk.Button(root, text = "6",
                                  command = lambda:self.button_press('6')).grid(row = 2, column = 2)

        self.buttonMult = ttk.Button(root, text = "*",
                                    command = lambda:self.math_button_press('*')).grid(row = 2, column = 3)

        # Start of the third row

        self.button1 = ttk.Button(root, text = "1",
                                  command = lambda:self.button_press('1')).grid(row = 3, column = 0)

        self.button2 = ttk.Button(root, text = "2",
                                  command = lambda:self.button_press('2')).grid(row = 3, column = 1)

        self.button3 = ttk.Button(root, text = "3",
                                  command = lambda:self.button_press('3')).grid(row = 3, column = 2)

        self.buttonAdd = ttk.Button(root, text = "+",
                                    command = lambda:self.math_button_press('+')).grid(row = 3, column = 3)

        # Start of the fourth row

        self.buttonAC = ttk.Button(root, text = "AC",
                                    command = lambda:self.clear_button_press()).grid(row = 4, column = 0)

        self.button0 = ttk.Button(root, text = "0",
                                    command = lambda:self.button_press('0')).grid(row = 4, column = 1)

        self.buttonEqual = ttk.Button(root, text = "=",
                                    command = lambda:self.equal_button_press()).grid(row = 4, column = 2)

        self.buttonSub = ttk.Button(root, text = "-",
                                    command = lambda:self.math_button_press('-')).grid(row = 4, column = 3)

root = Tk()
calc = Personal_Calculator(root)

root.mainloop()