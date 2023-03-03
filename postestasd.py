import random #library

def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2  #digunakan untuk membagi len menjadi 2 atau membagi nilai tengah
        left_data = data[:mid] #untuk mengambil data dari tengah ke kiri
        right_data = data[mid:]#untuk megambil data dari tengah ke kanan

        mergesort(left_data)# untuk memanggil fungsi mgsort data kiri
        mergesort(right_data)# untuk memanggil fungsi mgsort data kanan

        i=j=k= 0#menyatakan bahwa index kiri,kanan,index penggabungan = 0

        while i < len(left_data) and j < len(right_data):
            if left_data[i] < right_data[j]:
                data[k] = left_data[i]
                i += 1
            else :
                data[k] = right_data[j]
                j +=1
            k +=1

        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k +=1
 
        while j < len(right_data):
            data[k] = right_data[j]
            j +=1
            k +=1

random.seed(1)#agar angka yg ke random hanya 1x saja
#Melakukan sorting pada variabel list dengan value bertipe data integer saja
data = [37, 92, 28, 52, 35, 83, 77, 80, 68, 46, 32]#data yg diambil secara random antara angka 20-100
mergesort(data)
print('data sebelum di mergesort:' ,[random.randint(20, 100) for i in range(11)])#digunakan untuk memanggil angka-angka random dari 20-100
print("data sesudah d mergesort:" , data)#untuk mendapatkan sample dari data yg telah diambil 
print(70*"=")

def quicksort(arr):
     if len (arr) <= 1:
        return arr
     else:

        pivot = arr[0]#mendapatkan index untuk membagi partisi

        left = [x for x in arr [1:] if x <= pivot]#quicksorting partisi kiri (lebih kecil dari pivot)

        right = [x for x in arr [1:] if x >= pivot]#quicksorting partisi kanan (lebih besar dari pivot)

        return quicksort(left) + [pivot] + quicksort(right)#mengembalikan partisi dimana partisi dilakukan
     
random.seed(1)#agar angka yg ke random hanya 1x saja
print('data sebelum di quicksort:' ,[random.randint(10,90) for i in range(11)]) #untuk mengambil angka random dari 10-90


arr =  [27, 82, 18, 42, 25, 73, 67, 70, 58, 36, 22]#data angka yg telah diambil dari random
a= quicksort(arr)
print('data setelah di quicksort: ', a)
print(70*"=")

def shell(list):
    n = len (list)
    gap = n // 2#Menentukan jarak lompatan index berdasarkan pembagian panjang data

    while gap > 0:
        for i in range (gap, n): #Menginisiasi index i
            temp = list[i] # Mengambil dari index i
            j=i #Inisiasi index j
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]#Menginisiasi value index j dengan value dengan index (j-gap)
                j -= gap #Untuk menghentikan perulangan


            list [j] = temp#untuk Menginisiasikan value index j dengan value index i
        gap //= 2 #Memperkecil gap

    return list

     
random.seed(1)#agar angka yg ke random hanya 1x saja
print('data sebelum di sort:' ,[random.randint(20,90) for i in range(11)]) 
#Melakukan sorting pada variabel list dengan value bertipe data integer saja
print ("data sesudah di sort : ", shell([27, 82, 18, 42, 25, 73, 67, 70, 58, 36, 22] ))
