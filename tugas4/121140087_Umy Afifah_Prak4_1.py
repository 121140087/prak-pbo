class Komputer:
  def __init__(self, nama, merk, jenis, harga):
    self.nama=nama
    self.jenis=jenis
    self.harga=harga
    self.merk=merk

class Processor(Komputer):
  def __init__(self, merk, jenis, harga, jumlah_core, kecepatan_processor):
    super().__init__("Processor", merk, jenis, harga)
    self.jumlah_core=jumlah_core
    self.kecepatan_processor=kecepatan_processor

  def tampil(self):
        print(f"{self.nama} {self.jenis} produksi {self.merk}")

class RAM(Komputer):
  def __init__(self, merk, jenis, harga, kapasitas_RAM):
    super().__init__("RAM", merk, jenis, harga)
    self.kapasitas_RAM=kapasitas_RAM
    
  def tampil(self):
        print(f"{self.nama} {self.jenis} produksi {self.merk}")

class HDD(Komputer):
  def __init__(self, merk, jenis, harga, kapasitas_HDD, rpm_HDD):
    super().__init__("SATA", merk, jenis, harga)
    self.kapasitas_HDD=kapasitas_HDD
    self.rpm_HDD=rpm_HDD

  def tampil(self):
        print(f"{self.nama} {self.jenis} produksi {self.merk}")

class VGA(Komputer):
  def __init__(self, merk, jenis, harga, kapasitas_VGA):
    super().__init__("VGA", merk, jenis, harga)
    self.kapasitas_VGA=kapasitas_VGA

  def tampil(self):
        print(f"{self.nama} {self.jenis} produksi {self.merk}")

class PSU(Komputer):
  def __init__(self, merk, jenis, harga, daya_PSU):
    super().__init__("PSU", merk, jenis, harga)
    self.daya_PSU=daya_PSU

  def tampil(self):
        print(f"{self.nama} {self.jenis} produksi {self.merk}")

p1 = Processor("Intel", "Core i7 7740X", 4350000, 4, "4.3GHz")
p2 = Processor("AMD", "Ryzen 5 3600", 250000, 4, "4.3GHz")
ram1 = RAM("V-Gen","DDR4 SODimm PC19200/2400MHz",328000,"4GB")
ram2 = RAM("G.SKILL","DDR4 2400MHz",328000,"4GB")
hdd1 = HDD("Seagate","HDD 2.5 inch",295000,"500GB",7200)
hdd2 = HDD("Seagate","HDD 2.5 inch",295000,"1000GB",7200)
vga1 = VGA("Asus","VGA GTX 1050",250000,"2GB")
vga2 = VGA("Asus","1060Ti",250000,"8GB")
psu1 = PSU("Corsair","Corsair V550",250000,"500W")
psu2 = PSU("Corsair","Corsair V550",250000,"500W")

rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

for x in range(len(rakit)):
    print("Komputer", x+1, ":")
    for y in range(len(rakit[x])):
        rakit[x][y].tampil()
    print()
