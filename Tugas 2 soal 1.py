#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Daftar_Kontak():
    print ("Nama: Jennie") 
    print ("No. Telephone: 09890897388") 
    print ("Nama: Jisoo") 
    print ("No. Telephone: 08261720")

def Tambah_Kontak():
    Nama = str(input("Nama Anda: "))
    No = int(input("No. Telephone: "))
    
def Keluar():
    print ("Program selesai, sampai jumpa!")

def show_Menu():
    print ("\nSelamat Datang")
    print ("================")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")
    
def Menu():
    while True:
        show_Menu()
        choice = input("Pilih Menu: ").lower()
        if choice == '1':
            Daftar_Kontak()
        elif choice == '2':
            Tambah_Kontak()
        elif choice == '3':
            Keluar()
        else:
            print(f': <{choice}>, Menu Tidak Tersedia')

if __name__ == '__main__':
    Menu()


# In[ ]:




