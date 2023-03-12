class KTP:
    _asalKTP={62:"INDONESIA", 12:"USA", 23:"CANADA"} #atribut kelas yang hanya dapat diakses dalam kelas ini saja.
                                                    #apabila ingin mengaksesnya harus menggunakan KTP._asalKTP
    
    def __init__(self, NIK, nama, alamat):
        self.__NIK=NIK
        self.nama=nama
        self._alamat=alamat
        
    def _ceknegara(self, kodenegara): #privat method dapat diakses seperti public method
        if kodenegara in KTP._asalKTP:
            print(f"Kode Negara dari {self.__NIK} adalah {KTP._asalKTP[kodenegara]}") #contoh akses _asalKTP
        
    def tampil(self):
        print("Nama  : ", self.nama)
        print("NIK   : ", self.__NIK) #atribut privat hanya dapat diakses dalam kelas
        print("Alamat: ", self._alamat)

data=int(input("Berapa banyak data: "))
for i in range(data):
    NIK=int(input("No NIK (4 digit): "))
    if len(str(NIK)) == 4: 
        nama=input("Nama : ")
        alamat=input("Alamat : ")
        rakyat=KTP(NIK, nama, alamat)
        rakyat.tampil() #merupakan method public maka dapat di akses di luar kelas
        kode=NIK//100 
        rakyat._ceknegara(kode)#merupakan method proctect maka dapat di akses di luar kelas
    else:
        print("Jumlah digit NIK tidak tepat")
        breakpoint

#print(rakyat.__NIK) merupakan atribut privat, maka tidak dapat diakses di luar kelas tersebut
#maka penggunaan atribut/method yang privat tidak dapat diakses pada luar kelas tidak sama seperti public dan proctect
        
