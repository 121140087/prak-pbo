class Robot:
  jumlah_turn=0
  def __init__(self, nama, health, damage):
    self.nama=nama
    self.health=health
    self.damage=damage

  def lakukan_aksi(self, lawan):
    if self.nama=="Antares":
      damage=self.damage
      if self.jumlah_turn%3==0:
        damage*=1.5
      lawan.terima_aksi(damage)
      if self == myhero:
        print(f"Robotmu ({self.nama}) menyerang sebanyak {damage} DMG")
      elif self == enemy:
        print(f"Robot lawan ({self.nama}) menyerang sebanyak {damage} DMG")
    if lawan.health <= 0:
      if self == myhero:
        print(f"Robotmu ({self.nama}) mengalahkan robot lawan ({lawan.nama})")
      elif self == enemy:
        print(f"Robot lawan ({self.nama}) mengalahkan robotmu ({lawan.nama})")
        
    elif self.nama=="Alphasetia":
      damage=self.damage
      if self.jumlah_turn%2==0:
        self.health+=4000
        if self == myhero:
          print(f"Robotmu ({self.nama}) menambah darah sebanyak 4000 HP")
        elif self == enemy:
          print(f"Robot lawan ({self.nama}) menambah darah sebanyak 4000 HP")
      lawan.terima_aksi(damage)
      if self == myhero:
        print(f"Robotmu ({self.nama}) menyerang sebanyak {damage} DMG")
      elif self == enemy:
        print(f"Robot lawan ({self.nama}) menyerang sebanyak {damage} DMG")

      if lawan.health <= 0:
        if self == myhero:
          print(f"Robotmu ({self.nama}) mengalahkan robot lawan ({lawan.nama})")
        elif self == enemy:
          print(f"Robot lawan ({self.nama}) mengalahkan robotmu ({lawan.nama})")

    elif self.nama=="Lecalicus":
      damage=self.damage
      if self.jumlah_turn%4==0:
        self.health+=7000
        damage*=2
        if self == myhero:
          print(f"Robotmu ({self.nama}) menambah darah sebanyak 7000 HP")
        elif self == enemy:
          print(f"Robot lawan ({self.nama}) menambah darah sebanyak 7000 HP")
      lawan.terima_aksi(damage)
      if self == myhero:
        print(f"Robotmu ({self.nama}) menyerang sebanyak {damage} DMG")
      elif self == enemy:
        print(f"Robot lawan ({self.nama}) menyerang sebanyak {damage} DMG")
      if lawan.health <= 0:
        if self == myhero:
          print(f"Robotmu ({self.nama}) mengalahkan robot lawan ({lawan.nama})")
        elif self == enemy:
          print(f"Robot lawan ({self.nama}) mengalahkan robotmu ({lawan.nama})")

  def terima_aksi(self, damage):
    self.health-=damage
      

class Robot1(Robot):
  def __init__(self, nama="Antares", health=50000, damage=5000):
    super().__init__(nama, health, damage)

class Robot2(Robot):
  def __init__(self, nama="Alphasetia", health=40000, damage=6000):
    super().__init__(nama, health, damage)
    
class Robot3(Robot):   
  def __init__(self, nama="Lecalicus", health=45000, damage=5500):
    super().__init__(nama, health, damage)
  

print("Selamat datang di pertandingan robot Yamako")
hero=int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :"))
lawan=int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :"))

if hero == 1:
  myhero=Robot1()
elif hero == 2:
  myhero=Robot2()
elif hero == 3:
  myhero == Robot3()
else :
  print("Robot tidak terdeteksi")

if lawan == 1:
  enemy=Robot1()
elif lawan == 2:
  enemy=Robot2()
elif lawan == 3:
  enemy=Robot3()
else :
  print("Robot tidak terdeteksi")

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
print("")
while myhero.health>0 and enemy.health>0:
  Robot.jumlah_turn+=1
  print("Turn saat ini :",Robot.jumlah_turn)
  print(f"Robotmu ({myhero.nama} - {myhero.health}), robot lawan ({enemy.nama} - {enemy.health})")
  suithero=int(input(f"Pilih tangan robotmu ({myhero.nama}) :"))
  suitenemy=int(input(f"Pilih tangan robot lawan ({enemy.nama}) :"))
  if suithero == 1:
    if suitenemy ==1:
      print("Seri!!")
    elif suitenemy==2:
      enemy.lakukan_aksi(myhero)
    elif suitenemy==3:
      myhero.lakukan_aksi(enemy)
    else:
      print("Error!!")
      Robot.jumlah_turn-=1
  elif suithero == 2:
    if suitenemy ==2:
      print("Seri!!")
    elif suitenemy==1:
      myhero.lakukan_aksi(enemy)
    elif suitenemy==3:
      enemy.lakukan_aksi(myhero)
    else:
      print("Error!!")
      Robot.jumlah_turn-=1
  elif suithero == 3:
    if suitenemy ==3:
      print("Seri!!")
    elif suitenemy==1:
      enemy.lakukan_aksi(myhero)
    elif suitenemy==2:
      myhero.lakukan_aksi(enemy)
    else:
      print("Error!!")
      Robot.jumlah_turn-=1
  else:
    print("Error!!")
    Robot.jumlah_turn-=1
  print("")
