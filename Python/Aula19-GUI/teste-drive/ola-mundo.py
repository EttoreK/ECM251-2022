import ttkbootstrap as ttk
from tkinter import PhotoImage

base = ttk.Window(
	title="Minha GUI Mauá",
	size=(1024,400),
	position=(100,100),
	minsize=(600,300),
	maxsize=(2400,1200),
	alpha=1,
	iconphoto="calc_ic.png"
)

#base.iconphoto(False, PhotoImage(file="calc_ic.png"))
base.mainloop()