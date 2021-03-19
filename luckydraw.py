import random

print('Selamat datang di Lucky Draw')
print('Semoga Beruntung')

x = int(input("Silahkan masukkan berapa kali percobaan yang anda inginkan = "))
y = 0
y1 = [ ]

while y < x:
    y += 1    
    z = random.randint (1,100)
    print('Percobaan ke {}.'.format(y), end=" ")

    if z <= 100 and z > 80:
        print ("(*), Kurang beruntung ")
        y1.append("1")
        
    elif z <= 80 and z > 60:
        print ("(**), Coba lagi ")
        y1.append("2")
        
    elif z <= 60 and z > 30:
        print ("(***), Lumayan ")
        y1.append("3")
        
    elif z <= 30 and z > 1:
        print ("(****), Sedikit lagi ")
        y1.append("4")
        
    elif z == 1:
        print ("(*****), Selamat! anda mendapatkan Hadiah Spesial ")
        y1.append("5")

print("\nJumlah Bintang 1 =", y1.count("1"))
print("Jumlah Bintang 2 =", y1.count("2"))
print("Jumlah Bintang 3 =", y1.count("3"))
print("Jumlah Bintang 4 =", y1.count("4"))
print("Jumlah Bintang 5 =", y1.count("5"))

input("\nPress Enter to Exit")
    