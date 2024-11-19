import tkinter as tk
from tkinter import *

# Dữ liệu mẫu cho danh sách nhà tuyển dụng và danh sách người tìm việc
var = ["Variables", "Variables are containers for storing data values.",
             "Creating Variables", "cnpm has no command for declaring a variable.",
             "A variable is created the moment you first assign a value to it.",
             "x = 5",
             "y = 'John'",
             "print(x)",
             "print(y)"]

data = ["Built-in Data Types", "In programming, data type is an important concept.",
        "Variables can store data of different types, and different types can do different things.",
        "cnpm has the following data types built-in by default, in these categories:",
        "Text Type:	str",
        "Numeric Types:	int, float, complex",
        "Sequence Types:	list, tuple, range",
        "Mapping Type:	dict",
        "Set Types:	set, frozenset",
        "Boolean Type:	bool",
        "Binary Types:	bytes, bytearray, memoryview",
        "None Type:	NoneType",
        "Print the data type of the variable x:",
        "x = 5",
        "print(type(x))"]
string = ["Strings",
          "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
          "'hello' is the same as 'hello'.",
          "You can display a string literal with the print() function:",
          "ExampleGet your own cnpm Server",
          "print('Hello')",
          "print('Hello')"]

list = ["mylist = ['apple', 'banana', 'cherry']",
        "List",
        "Lists are used to store multiple items in a single variable.",
        "Lists are one of 4 built-in data types in cnpm used to store collections of data,",
        "the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.",
        "Lists are created using square brackets:",
        "ExampleGet your own cnpm Server"
        "Create a List:",
        "thislist = ['apple', 'banana', 'cherry']",
        "print(thislist)"]
Tuple = ["mytuple = ('apple', 'banana', 'cherry')",
         "Tuple",
         "Tuples are used to store multiple items in a single variable.",
         "Tuple is one of 4 built-in data types in cnpm used to store collections of data,",
         "the other 3 are List, Set, and Dictionary, all with different qualities and usage.",
         "A tuple is a collection which is ordered and unchangeable.",
         "Tuples are written with round brackets.",
         "ExampleGet your own cnpm Server",
         "Create a Tuple:",
         "thistuple = ('apple', 'banana', 'cherry')"
         "print(thistuple)"]

Set = ["myset = {'apple', 'banana', 'cherry'}",
       "Set",
       "Sets are used to store multiple items in a single variable.",
       "Set is one of 4 built-in data types in cnpm used to store collections of data,"
       "the other 3 are List, Tuple, and Dictionary, all with different qualities and usage."
       "A set is a collection which is unordered, unchangeable*, and unindexed.",
       "* Note: Set items are unchangeable, but you can remove items and add new items.",
       "Sets are written with curly brackets.",
       "ExampleGet your own cnpm Server",
       "Create a Set:",
       "thisset = {'apple', 'banana', 'cherry'}",
       "print(thisset)"]
Dictionaries = ["cnpm Dictionaries",
                "thisdict = {",
                "brand: Ford",
                "model: 'Mustang'",
                "year: 1964",
                "}"
                ]
if_else = ["Equals: a == b",
           "Not Equals: a != b",
           "Less than: a < b",
           "Less than or equal to: a <= b",
           "Greater than: a > b",
           "Greater than or equal to: a >= b"]

while_loops = ["while loops",
               "for loops",
               "i = 1",
               "while i < 6:",
               "print(i)",
               "i += 1"]
For_Loops = ["A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)",
             "This is less like the for keyword in other programming languages,",
             "and works more like an iterator method as found in other object-orientated programming languages.",
             "With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.",
             "Print each fruit in a fruit list:",
             "fruits = ['apple', 'banana', 'cherry']",
             "for x in fruits:",
             "print(x)"
             ]
Functions =["A function is a block of code which only runs when it is called.",
            "You can pass data, known as parameters, into a function.",
            "A function can return data as a result.",
            "In cnpm a function is defined using the def keyword:",
            "def my_function():",
            "print('Hello from a function')"]
Classes_and_Objects = ["cnpm is an object oriented programming language.",
                       "Almost everything in cnpm is an object, with its properties and methods.",
                       "A Class is like an object constructor, or a 'blueprint' for creating objects.",
                       "Create a class named MyClass, with a property named x:",
                       "class MyClass:",
                       "x = 5"]


def show_Variable():
    listbox.delete(0, tk.END)
    for employer in var:
        listbox.insert(tk.END, employer)


def show_data():
    listbox.delete(0, tk.END)
    for seeker in data:
        listbox.insert(tk.END, seeker)


def show_string():
    listbox.delete(0, tk.END)
    for seeker in string:
        listbox.insert(tk.END, seeker)


def show_list():
    listbox.delete(0, tk.END)
    for seeker in list:
        listbox.insert(tk.END, seeker)


def show_Tuple():
    listbox.delete(0, tk.END)
    for seeker in Tuple:
        listbox.insert(tk.END, seeker)


def show_Set():
    listbox.delete(0, tk.END)
    for seeker in Set:
        listbox.insert(tk.END, seeker)


def show_Dictionaries():
    listbox.delete(0, tk.END)
    for seeker in Dictionaries:
        listbox.insert(tk.END, seeker)


def show_ifelse():
    listbox.delete(0, tk.END)
    for seeker in if_else:
        listbox.insert(tk.END, seeker)


def show_while():
    listbox.delete(0, tk.END)
    for seeker in while_loops:
        listbox.insert(tk.END, seeker)


def show_for():
    listbox.delete(0, tk.END)
    for seeker in For_Loops:
        listbox.insert(tk.END, seeker)


def show_function():
    listbox.delete(0, tk.END)
    for seeker in Functions:
        listbox.insert(tk.END, seeker)


def show_cao():
    listbox.delete(0, tk.END)
    for seeker in Classes_and_Objects:
        listbox.insert(tk.END, seeker)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("cnpm Tutorial")
root.geometry("600x650")

# Tạo frame cho menu bên trái
menu_frame = tk.Frame(root, width=200, bg="lightgray")
menu_frame.pack(side="left", fill="y")

# Tạo frame cho nội dung hiển thị
content_frame = tk.Frame(root)
content_frame.pack(side="right", expand=True, fill="both")

# Thêm các nút vào menu
btn_Variable = tk.Button(menu_frame, text="cnpm Variable", command=show_Variable)
btn_Variable.pack(pady=10)

btn_DataTypes= tk.Button(menu_frame, text="cnpm Data Types", command=show_data)
btn_DataTypes.pack(pady=10)

btn_Number= tk.Button(menu_frame, text="cnpm String", command=show_string)
btn_Number.pack(pady=10)

btn_List= tk.Button(menu_frame, text="cnpm List", command=show_list)
btn_List.pack(pady=10)

btn_Tuple= tk.Button(menu_frame, text="cnpm Tuple", command=show_Tuple)
btn_Tuple.pack(pady=10)

btn_Set= tk.Button(menu_frame, text="cnpm Set", command=show_Set)
btn_Set.pack(pady=10)

btn_Dictionaries= tk.Button(menu_frame, text="cnpm Dictionaries", command=show_Dictionaries)
btn_Dictionaries.pack(pady=10)

btn_ifelse= tk.Button(menu_frame, text="cnpm If... else", command=show_ifelse)
btn_ifelse.pack(pady=10)

btn_while= tk.Button(menu_frame, text="cnpm While loops", command=show_while)
btn_while.pack(pady=10)

btn_for= tk.Button(menu_frame, text="cnpm For loops", command=show_for)
btn_for.pack(pady=10)

btn_function= tk.Button(menu_frame, text="cnpm For loops", command=show_function)
btn_function.pack(pady=10)

btn_cao= tk.Button(menu_frame, text="cnpm Class And Object", command=show_cao)
btn_cao.pack(pady=10)

btn_thoat= tk.Button(menu_frame, text="Exit", command=exit)
btn_thoat.pack(pady=10)

# Tạo listbox để hiển thị danh sách
listbox = tk.Listbox(content_frame)
listbox.pack(expand=True, fill="both", padx=20, pady=20)

# Khởi động giao diện
root.mainloop()
