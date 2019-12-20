"""
    Transformasi Angka, Karakter, dan String 
    Date    : Wednesday, 11/12/2019
    Author  : Pasyah Vegananda
    GitHub  : PVegananda
    
"""

#Transformasi 

"""
pada angka transformasi dilakukan dengan
zfill(). Berguna untuk menambahkan 0 di 
depan angka-angka yang dituju misal angka
1 menjadi 0001 , angka 101 menjadi 00101.
Tetapi x harus berupa int
"""

x = 1 #membuat int yang berisi angka 1
x = str(x) #mengkonversi x menjadi str
b = x.zfill(3) #menambahkan 0 diposisi x index ke - 2
print(x)
print(b)



"""
pada string transformasi dapat menggunakan
perintah upper() dan lower().
"""

kata = "Hei python!"
kata = kata.upper()
print(kata , end=" = " )
if (kata.isupper()):
    print("HURUF KAPITAL")
else:
    print("null")
kata = kata.lower()
print(kata, end = " = ")
if (kata.isupper()):
    print("null")
else:
    print("huruf kecil")