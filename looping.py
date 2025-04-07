def hitung_LuasSegitiga():
    try:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah:", luas)
    except ValueError:
        print("Masukkan angka")

def hitung_luas_PersegiPanjang():
    try:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        print("Luas persegi panjang adalah:", luas)
    except ValueError:
        print("Masukkan angka")

def tentukan_GanjilGenap():
    try:
        bilangan = int(input("Masukkan sebuah angka bulat: "))
        if bilangan % 2 == 0:
            print(bilangan, "adalah bilangan genap.")
        else:
            print(bilangan, "adalah bilangan ganjil.")
    except ValueError:
        print("Masukkan bilangan bulat")

def main():
    while True:
        print("\n" + "-" * 15)
        print("Menu:")
        print("1. Hitung luas segitiga")
        print("2. Hitung luas persegi panjang")
        print("3. Menentukan bilangan ganjil atau genap")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
        
        if pilihan == "1":
            hitung_LuasSegitiga()
        elif pilihan == "2":
            hitung_luas_PersegiPanjang()
        elif pilihan == "3":
            tentukan_GanjilGenap()
        elif pilihan == "4":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")
            
        print("\n")

if __name__ == "__main__":
    main()
