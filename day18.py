#membuat set sederhana

exo = {"suho","chanyeol","kyungsu","sehun",123}
print(exo)

exo.add("kay")
print(exo)

#contoh set pada integer
genap = {2,4,6,8,10}
ganjil = {1,3,5,7,9}
prima = {2,3,5,7}

print(genap.union(ganjil))
print(genap|ganjil)
print(genap.intersection(ganjil))
print(genap.intersection(prima))

#list
#menambah isi list berdasarkan panjang list

nilai = int(input("masukkan panjang list :"))
list=[]
print("list awal :{} ")
for i in range(nilai):
     total = int(input("masukkan nilai list pada index ke-" + str(i)  + ":"))
     list.insert(i,total)

print(list)
    



