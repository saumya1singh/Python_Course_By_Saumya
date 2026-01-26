# import tkinter for creating GUI apps 
import tkinter as tk 
from tkinter import filedialog, messagebox 

# Main window code 
root= tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# create text area 
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 18)
)

text.pack(expand=True,fill=tk.BOTH)

#Main Logic starts now 

# Function 1 - to create a new file 
def new_file():
    text.delete(1.0, tk.END)

# Function 2 - to open a new file 
def open_file():
    # open file dialogue 
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        #open selected file 
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Function 3 - save the file 

def save_file():
    #open save file dialogue 
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully")

# Create Menu Bar 
menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

# New, Open File, Save , Exit 

# add filemenu to menu bar 
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# starts and keeps the window open
root.mainloop()













