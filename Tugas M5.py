#No 1 
jadwal_hari=("senin","selasa","rabu","kamis","jumat")
print(type(jadwal_hari))

#No 2
koordinat=(10,20,30,40,50)
print(koordinat[2])
print(koordinat[-2:])

#No 3 (ERROR)
warna=("Merah","Kuning","Hijau")
warna[0]="Biru"
#No 4
huruf=("a","b","c","a","d","a","e")
print(f'index huruf \"d\":{huruf.index("d")}')
print(f'banyaknya huruf \"a\":{huruf.count("a")}')

#No 5 
titik_lokasi=(112.79,-7.28)
(longitude,latitude)=titik_lokasi
print(f'longitude:{longitude}')
print(f'latitude:{latitude}')

#No 6
kendaraan=("Motor","Mobil","Sepeda")
list_kendaraan=list(kendaraan)
list_kendaraan[1]="Bus"
kendaraan=tuple(list_kendaraan)
print(kendaraan)