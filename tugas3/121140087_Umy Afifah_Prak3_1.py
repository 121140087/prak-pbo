class AkunBank:
  list_pelanggan={} #untuk menyimpan data pelanggan
  def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
    self.__no_pelanggan=no_pelanggan
    self.__nama_pelanggan=nama_pelanggan
    self.__jumlah_saldo=jumlah_saldo
    self.list_pelanggan.update({self.__no_pelanggan:self.__nama_pelanggan})
    self.menu=0
    
  def lihat_saldo(self):
    print(f"{self.__nama_pelanggan}, memiliki saldo Rp {self.__jumlah_saldo}")
    
  def tarik_tunai(self):
    self.tarik=int(input("Nominal yang ingin ditarik: "))
    if self.tarik > self.__jumlah_saldo:
      print("Nominal saldo yang Anda punya tidak cukup")
    else:
      print("Saldo berhasil ditarik")
      self.__jumlah_saldo-=self.tarik
      
  def transfer(self):
    self.kirim=int(input("Masukkan nominal yang ingin ditransfer: "))
    if self.kirim <= self.__jumlah_saldo:
      
      self.noatm=int(input("Masukkan no rekening tujuan: "))
      if self.noatm in AkunBank.list_pelanggan:
        print("Transfer Rp", self.kirim,"ke", AkunBank.list_pelanggan[self.noatm],"sukses!")
        self.__jumlah_saldo-=self.kirim
      else:
        print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")
    
  def lihat_menu(self):
    print("Selamat datang di Bank Jago")
    print("Halo", self.__nama_pelanggan,"Apa yang ingin anda lakukan?")
    print("1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Keluar")
    self.menu=int(input("Masukkan pilihan: "))
    if self.menu == 1:
      AkunBank.lihat_saldo(self)
    elif self.menu == 2:
      AkunBank.tarik_tunai(self)
    elif self.menu == 3:
      AkunBank.transfer(self)

Akun1=AkunBank(1234, "Umy Afifah", 5000000000)
Akun2=AkunBank(2345, "Ukraina", 6666666666)
Akun3=AkunBank(3456, "Elon Musk", 9999999999)

while Akun1.menu < 4:
  Akun1.lihat_menu()
  print()
