class Mahasiswa:
    def __init__(self, nama, nim, kelas, jumlah_sks):
      self.nama=nama
      self.nim=nim
      self.kelas=kelas
      self.jumlah_sks=jumlah_sks

    def hitungnim(self):
      print("Jumlah nim :",len(self.nim))
    
    def pindah(self, kelas):
      self.kelas=kelas
        
    def display(self):
      print("Nama :", self.nama)
      print("NIM :", self.nim)
      print("Kelas :", self.kelas)
      print("Jumlah SKS :", self.jumlah_sks)

nama=input("Masukkan nama : ")
nim=input("Masukkan nim : ")
kelas=input("Masukkan kelas : ")
jumlah_sks=int(input("Masukkan jumlah sks : "))
umy=Mahasiswa(nama, nim, kelas, jumlah_sks)
umy.display()

ganti=input("Apakah anda ingin mengganti kelas? ya/no : ")
if ganti == "ya":
  umy.kelas=input("Masukkan kelas baru : ")
  umy.display()

hitung=input("Apakah anda ingin menghitung jumlah nim? ya/no : ")
if hitung == "ya":
  umy.hitungnim()
  
