from abc import ABC, abstractclassmethod

class AkunBank(ABC):
  def __init__(self, nama, tahun_daftar, saldo):
    self.nama=nama
    self.tahun_daftar=tahun_daftar
    self.saldo=saldo

  def lihat_saldo(self):
    print("Akun dengan nama", self.nama)
    print("memiliki saldo", self.saldo)

  @abstractclassmethod
  def transfer_saldo(self):
    pass

  @abstractclassmethod
  def lihat_suku_bunga(self):
    pass

class AkunGold(AkunBank):
  def __init__(self, nama, tahun_daftar, saldo):
    super().__init__(nama, tahun_daftar, saldo)
    self.usia=2023-self.tahun_daftar
    
  def transfer_saldo(self, jumlah):
    if self.usia >= 3 and jumlah > 100000:
      print("Biaya admin gratis")
      self.saldo-=jumlah
      
    elif self.usia < 3 and jumlah > 100000:
      print("Biaya admin Rp. 2000")
      self.saldo-=(jumlah+2000)
      
    else:
      print("Biaya admin gratis")
      self.saldo-=jumlah

  def lihat_suku_bunga(self):
    if self.usia >= 3 and self.saldo >= 1000000000:
      self.bunga=self.saldo*0.01
      
    elif self.usia < 3 and self.saldo >= 1000000000:
      self.bunga=self.saldo*0.02
      
    else:
      self.bunga=self.saldo*0.03
    print("Suku bunga :", self.bunga)
    
class AkunSilver(AkunBank):
  def __init__(self, nama, tahun_daftar, saldo):
    super().__init__(nama, tahun_daftar, saldo)
    self.usia=2023-self.tahun_daftar
    
  def transfer_saldo(self, jumlah):
    if self.usia >= 3 and jumlah > 100000:
      print("Biaya admin Rp. 2000")
      self.saldo-=(jumlah+2000)
      
    elif self.usia < 3 and jumlah > 100000:
      print("Biaya admin Rp. 5000")
      self.saldo-=(jumlah+5000)
      
    else:
      print("Biaya admin gratis")
      self.saldo-=jumlah

  def lihat_suku_bunga(self):
    if self.usia >= 3 and self.saldo >= 10000000:
      self.bunga=self.saldo*0.01
      
    elif self.usia < 3 and self.saldo >= 10000000:
      self.bunga=self.saldo*0.02
      
    else:
      self.bunga=self.saldo*0.03
    print("Suku bunga :", self.bunga)

Akun1=AkunGold("Umy", 2010, 1000000000)
Akun2=AkunSilver("Afifah", 2019, 1000000000)
Akun1.transfer_saldo(200000)
Akun1.lihat_suku_bunga()
Akun1.lihat_saldo()
print("")
Akun2.transfer_saldo(50000000)
Akun2.lihat_suku_bunga()
Akun2.lihat_saldo()