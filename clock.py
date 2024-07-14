import tkinter as tk
from time import strftime, localtime

def update_time():
    current_time = strftime('%I:%M:%S %p') 
    time_label.config(text=current_time)
    date_label.config(text=strftime('%d-%m-%Y'))  
    root.after(1000, update_time)  

root = tk.Tk()
root.title("Digital Clock")
root.geometry('300x150')
root.configure(bg='#e6e6fa')  

time_label = tk.Label(root, font=('Helvetica', 48, 'bold'), bg='#e6e6fa', fg='#333333')
date_label = tk.Label(root, font=('Helvetica', 14, 'italic'), bg='#e6e6fa', fg='#555555')

time_label.grid(row=0, column=0, pady=10)
date_label.grid(row=1, column=0, pady=5)

update_time()

root.mainloop()