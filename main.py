#-*-coding: utf-8-*-
from tkinter import *
from json import loads
with open("atoms.json", "r") as f:
	ATOMS = loads(f.read())
with open("symbols.json", "r") as f:
	SYMBOLS = loads(f.read())

def convert(element):
	if element in SYMBOLS:
		return SYMBOLS[element]
	return "-*-*-*-*-"


def calculate(element1, element2, show_process=False):
	element1 = element1.lower().strip()
	element2 = element2.lower().strip()
	errcounter = 0
	if element1 not in ATOMS or element2 not in ATOMS:
		element1 = convert(element1.title())
		element2 = convert(element2.title())
		if element1 not in ATOMS or element2 not in ATOMS:
			return "Check the spelling of the elements."
	electro_negativity1 = ATOMS[element1]
	electro_negativity2 = ATOMS[element2]
	difference = electro_negativity1 - electro_negativity2
	if difference < 0:
		difference *= -1	
	if show_process:
		print("{} -> {}".format(element1, electro_negativity1))
		print("{} -> {}".format(element2, electro_negativity2))
		print("Difference: {}".format(difference))
	
	
	if difference <= 0.4:
		return "Non-polar"
	elif difference <= 1.9:
		return "Polar"
	else:
		return "Ionic"


def main():
	root = Tk()
	root.geometry("500x500")
	root.title("By: Diego Perez")
	mframe = Frame(root, bg="#F2F2F2")
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	title = Label(mframe, bg="#F78181",text="Know your bond", font=("Arial", 18), fg="white")
	title.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
	entryshade = Label(mframe, bg="#F78181")
	entryshade.place(relx=0.15, rely=0.39, relwidth=0.7, relheight=0.07)
	firstelement = Entry(mframe)
	firstelement.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.05)
	secondelement = Entry(mframe)
	secondelement.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.05)


	root.mainloop()




if __name__ == '__main__':
	main()