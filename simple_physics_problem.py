import math

#persoalan gerak lurus
class GerakLurus():
    #disini merupakan class yang digunakan untuk menghitung besaran fisis berdasarkan konsep gerak lurus
    def __init__(self,kecepatan,waktu,jarak=None):
        self.kecepatan = kecepatan
        self.waktu = waktu
        self.jarak = jarak
    

    def hitung_jarak(self):
        hasil = self.kecepatan * self.waktu
        self.jarak = hasil
        print(f"Jarak yang ditempuh adalah : {hasil} m")
        return self.jarak
    

    def kecepatan_rata_rata(self):
        try:
            kecepatan_rata_rata = self.jarak/self.waktu
            print(f"Kecepatan rata ratanya adalah : {kecepatan_rata_rata} m/s")
        except TypeError:
            print("Buat variabel jarak terlebih dahulu")



#persoalan gerak parabolik
class GerakParabolik():
    #ini merupakan class untuk menghitung hasil besaran fisis berdasarkan konsep gerak parabolik
    def __init__(self,kecepatan_awal,sudut):
        self.kecepatan_awal = kecepatan_awal
        self.sudut = sudut
    
    
    def horizontal_maksimum(self,gravitasi=9.8):

        hasil = ((self.kecepatan_awal**2) * math.sin(2*self.sudut))/gravitasi
        self.jarak_horizontal_maksimum = hasil
        self.gravitasi = gravitasi
        print(f"Jarak horizontal maksimumnya adalah {round(self.jarak_horizontal_maksimum,2)}")
        return self.jarak_horizontal_maksimum

    
    def tinggi_maksimum(self):
        hasil = ((self.kecepatan_awal**2) * (math.sin(self.sudut)**2))/(2*self.gravitasi)
        print(f"Tinggi Maksimumnya adalah {round(hasil,2)}")
    

    
