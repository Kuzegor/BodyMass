from tkinter import *
from tkinter import messagebox
 
def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get())/100
   bmi = kg/(m*m)
   bmi = round(bmi, 1)
 
   if bmi < 18.5:
       messagebox.showinfo('bmi-pythonguides', f'IMT = {bmi} sootvetstvuet nedostatochnomu vesu')
   elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('bmi-pythonguides', f'IMT = {bmi} sootvetstvuet normalnomu vesu')
   elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('bmi-pythonguides', f'IMT = {bmi} sootvetstvuet izbytochnomu vesu')
   else:
       messagebox.showinfo('bmi-pythonguides', f'IMT = {bmi} sootvetstvuet ozhireniyu')  
 
window = Tk()
window.title('kalkulator indeksa massy tela ')
window.geometry('400x300')
 
 
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
 
 
height_lb = Label(
   frame,
   text="Vvedite svoy rost (v sm) "
)
height_lb.grid(row=3, column=1)
 
weight_lb = Label(
   frame,
   text="Vvedite svoy ves (v kg)  ",
)
weight_lb.grid(row=4, column=1)
 
height_tf = Entry(
   frame,
)
height_tf.grid(row=3, column=2, pady=5)
 
weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)
 
cal_btn = Button(
   frame,
   text='Raschitat IMT',
   command=calculate_bmi
)
cal_btn.grid(row=5, column=2)
 
window.mainloop()