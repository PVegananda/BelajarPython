"""
    Python Checker All Character
    Date    : Saturday, 14/12/2019
    Author  : Pasyah Vegananda
    GitHub  : PVegananda
    
"""

#Method of checking string method

string = "sebuahstring"
angka = "1234"
desimal = "12,34"
space = " "
tab = "\t"
newline = "\n"
whitespace = "     "
title = "Ini Adalah Judul"

check1 = string.isalpha()
check2 = angka.isdecimal()
check3 = angka.isalnum() and string.isalnum() 
check4 = space.isspace() and tab.isspace() and newline.isspace() and whitespace.isspace()
check5 = title.istitle()

print(check1)
print(check2)
print(check3)
print(check4)
print(check5)

#Checking Start and End of a String

"Depan Belakang".startswith("Depan")
"Depan Belakang".endswith("Belakang")
"Depan Belakang".startswith("Belakang")
"Depan Belakang".endswith("Depan")



