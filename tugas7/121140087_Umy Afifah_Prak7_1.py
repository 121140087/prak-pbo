import tkinter
from tkinter import filedialog as fd

def Save_file():
    try:
        text_file = fd.asksaveasfilename(defaultextension=".txt",
            filetypes=[("text file", "*.txt")])
        if not text_file:
            return
        with open(text_file, 'w') as file:
            file.write(my_text.get(1.0, tkinter.END))
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))
  
def Open_file():
    try:
        my_text.delete(1.0, tkinter.END)
        text_file = fd.askopenfilename(defaultextension=".txt",
            filetypes=[("text file", "*.txt")])
        if not text_file:
            return
        with open(text_file, "r") as file:
            stuff = file.read()
            my_text.insert(tkinter.END, stuff)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))

def Delete_all():
  my_text.delete(1.0, tkinter.END)

window=tkinter.Tk()
window.title("TUGAS PRAKTIKUM PBO")
window.geometry("650x500")

note=tkinter.Label(window, text="My Note")
note.grid(row = 0, column = 1)

my_text=tkinter.Text(window)
my_text.grid(row = 1, column = 1)

grid_bar = tkinter.Frame(window, relief=tkinter.RAISED, bd=2, bg="silver")

save_button=tkinter.Button(grid_bar, text="  Save  ", command=Save_file)
save_button.grid(row=1, column=0)

open_button=tkinter.Button(grid_bar, text=" Open ", command=Open_file)
open_button.grid(row=2, column=0)

delete_button=tkinter.Button(grid_bar, text="Delete ", command=Delete_all)
delete_button.grid(row=3, column=0)

grid_bar.grid(row=1, column=0, sticky="ns")
window.mainloop()
