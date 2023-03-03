cek=False
n=1;
user="informatika"
pword="12345678"

while cek==False :
  un=input("Username anda : ")
  pw=input("Password anda : ")

  if un==user and pw==pword:
    print("Berhasil login!")
    cek=True
  else :
    if n!=3:
      print("Username atau Password salah coba lagi.")
    else :
      print("Akun anda diblokir.")
      cek=True
    n+=1
