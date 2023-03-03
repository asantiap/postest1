import random

def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

        mergesort(left_data)
        mergesort(right_data)

        i=j=k= 0

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

random.seed(1)

data = [37, 92, 28, 52, 35, 83, 77, 80, 68, 46, 32]
mergesort(data)
print('data sebelum di mergesort:' ,[random.randint(20, 100) for i in range(11)])
print("data sesudah d mergesort:" , data)
print(70*"=")

def quicksort(arr):
     if len (arr) <= 1:
        return arr
     else:

        pivot = arr[0]

        left = [x for x in arr [1:] if x <= pivot]

        right = [x for x in arr [1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)
     
random.seed(1)
print('data sebelum di quicksort:' ,[random.randint(10,90) for i in range(11)]) 


arr =  [27, 82, 18, 42, 25, 73, 67, 70, 58, 36, 22]
a= quicksort(arr)
print('data setelah di quicksort: ', a)
print(70*"=")

def shell(list):
    n = len (list)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = list[i]
            j=i
            while j >= gap and list [j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap

            list [j] = temp
        gap //= 2

    return list

     
random.seed(1)
print('data sebelum di sort:' ,[random.randint(20,90) for i in range(11)]) 
print ("data sesudah di sort : ", shell([27, 82, 18, 42, 25, 73, 67, 70, 58, 36, 22] ))
