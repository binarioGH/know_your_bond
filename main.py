#-*-coding: utf-8-*-
from tkinter import *
from json import loads
with open("atoms.json", "r") as f:
	ATOMS = loads(f.read())

def calculate(elemen1, element2):
	if element1 not in ATOMS or element2 not in ATOMS:
		return "Check the spelling of the elements."
	difference = ATOMS[element1] - ATOMS[element2]
	if difference < 0:
		difference *= -1
	if difference >= 0.4:
		return "Non-polar"
	elif difference >= 1.9:
		return "Polar"
	else:
		return "Ionic"


def main():
	root = Tk()
	root.geometry("300x200")
	root.mainloop()




if __name__ == '__main__':
	main()