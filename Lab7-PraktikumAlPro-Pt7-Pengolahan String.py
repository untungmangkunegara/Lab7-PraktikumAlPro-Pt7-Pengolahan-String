#Pengolahan String
#71200619 Untung Mangkunegara
#Shella adalah seorang mahasiswa yang suka browsing soal meme. 
#Suatu hari dia melihat meme yang membuat huruf vokal berubah menjadi i dan memiliki keinginan untuk membuat 
#program untuk merubah huruf vokal menjadi i. 
#Karna Shella hanyalah seorang penyuka meme biasa dan tidak mengerti soal pemrograman 
#maka dia pun meminta anda sebagai seorang programmer untuk membantunya membuat program tersebut.
#SAYA MENGAMBIL SOAL DARI UG 7 KELAS A!
#input : masukkan kalimat
#proses : if
#output : iiiiiiiiiiii
#==================================================
kalimat=str(input("Masukkan satu kalimat yang ingin diubah: "))
kapital=0
non_kapital=0
#
for i in kalimat:
    if i.isupper()==True:
        kapital=kapital+1
    elif i.islower()==True:
        non_kapital=non_kapital+1
#
if kalimat=="a" or "u" or "e" or "o" or "A" or "U" or "E" or "O":
    kalimat=kalimat.replace("a","i")
    kalimat=kalimat.replace("u","i")
    kalimat=kalimat.replace("e","i")
    kalimat=kalimat.replace("o","i")
    kalimat=kalimat.replace("A","i")
    kalimat=kalimat.replace("U","i")
    kalimat=kalimat.replace("E","i")
    kalimat=kalimat.replace("O","i")
#
if kapital>non_kapital:
    kalimat=kalimat.upper()
    print(kalimat)
elif kapital<non_kapital:
    kalimat=kalimat.lower()
    print(kalimat)
    