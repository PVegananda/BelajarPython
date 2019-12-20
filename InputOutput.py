"""
    Input Output dalam Bahasa Python
    Date    : Saturday, 7/12/2019
    Author  : Pasyah Vegananda
    GitHub  : PVegananda
    
"""

print("Output Print") #Output menggunakan print

#Hasil

"""
Output Print

"""

var_1 = 5                    #Membuat Variabel var_1
print("The Value is", var_1) #Memberikan Output nilai value didalam var_1

#Hasil

"""
The Value is 5

"""

nama = "John"   #Membuat variable nama berisi str:John
umur = 15       #Membuat variable umur berisi int:15
print("%s is %d years old."%(nama, umur)) #Mencetak nama dan umur yang 
#didalam data pointer

#Hasil
"""
John is 15 years old.
"""

listku = [2,5,6]
print("list consist number of : %s " %listku)

#Hasil
"""

"""

#Beberapa specifier
"""
%s - String
%d - Integers
%f - Bilangan Pecahan
%.<digit>f - Bilangan pecahan dengan sejumlah digit angka dibelakang koma.
%x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

"""

num = input("Masukkan angka : ")
print(num)

#Hasil
"""
<num>

"""
#dua tipe angka
"""
int(10)     = 10
float(10)   = 10.0

"""

#int("2+3")  = error
#eval("2+3") = 5
