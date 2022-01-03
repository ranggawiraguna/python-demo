class mahasiswa :

    #Method-1 pada class mahasiswa, __init__ berfungsi sebagai konstruktor atau pembbuat object yang otomatis dijalankan pada saat
    #membuat object dari class mahasiswa
    def __init__(self):
        self.nim = input("Masukkan NIM Mahasiswa  : ")
        self.nama = input("Masukkan Nama Mahasiswa : ")

    #Method-2 pada class mahasiswa
    def inputNilai(self):
        self.nilaiAbsen = float(input("Masukkan Absen(%)      : "))
        self.nilaiTugas = float(input("Masukkan Nilai Tugas   : "))
        self.nilaiUTS = float(input("Masukkan Nilai UTS     : "))
        self.nilaiUAS = float(input("Masukkan Nilai UAS     : "))

    #Method-3 pada class mahasiswa
    def cekStatus(self, nama):
        totalNilai = self.nilaiAbsen + self.nilaiTugas + self.nilaiUTS + self.nilaiUAS

        if totalNilai < 56 :
            print("[!]Mahasiswa {} tidak lulus".format(nama))

        elif totalNilai < 100 :
            print("[!]Mahasiswa {} lulus".format(nama))

        else :
            print("[!]Terdapat kesalah pada inputNilai")


#Menggunakan Method melalui object mahasiswa1 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa1 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
mahasiswa1.inputNilai()
mahasiswa1.cekStatus(mahasiswa1.nama)

#Menggunakan Method melalui object mahasiswa2 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa2 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
mahasiswa2.inputNilai()
mahasiswa2.cekStatus(mahasiswa2.nama)

print(50*"=")
