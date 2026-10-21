import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - notepad")

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, file.read())
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def exit_app():
    if messagebox.askyesno("Quit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Untitled - notepad")
root.geometry("600x500")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root, undo=True, wrap="word")
text_area.pack(expand=True, fill="both")

root.mainloop()
