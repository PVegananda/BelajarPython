"""
    Duck Typing 
    Date    : Tuesday, 17/12/2019
    Author  : Pasyah Vegananda
    GitHub  : PVegananda
    
"""

#Make several words into sentence and reversed

word = "AkudanDia"
words = ["Aku","Adalah","Kucing"]
setences = "Aku Adalah Kucing"
paragraph = ''' Hari itu,
Aku menemukan anak kucing
Dipinggir Jalan
Sedang memakan tulang
Dan juga duduk
Diatas dedaunan yang rindang'''

print(", ".join(words))
print(" ".join(words))
print(setences.split(" "))
print(word.split("dan"))
print(paragraph.split("\n"))

print("\n")
#Mengedit teks paragraph

Teks = "Sebuah Kalimat"
print(Teks.rjust(20))
print(Teks.ljust(20, "*")) 
print(Teks.rjust(20, "*"))
print(Teks.center(20))
print(Teks.center(20, "="))

print("\n")
#Menghapus space kosong atau teks

kalimat  = "        Halo"
kalimat1 = "___ Halo Dunia _____"

print(kalimat.rstrip())
print(kalimat.strip())
print(kalimat.lstrip())
print(kalimat1.strip("_"))

print("\n")
#Mengganti string 

dua = "satu"
satu = "dua"

print(satu)
print(dua)
print(satu.replace("dua","satu"))
print(dua.replace("satu","dua"))
print(satu)
print(dua)
