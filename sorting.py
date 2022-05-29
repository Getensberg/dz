import random

list_ = [random.randint(1,1000) for i in range(40)]
list_1 =list(list_) 
list_2 = list(list_)

def bubbleSort(list_):


  	compare_count = 0
  	replace_count = 0
  	for i in range(len(list_)):
  		for j in range(0, len(list_) - i - 1):
  			if list_[j] > list_[j + 1]:
  				compare_count+=1
  				temp = list_[j]
  				list_[j] = list_[j+1]
  				list_[j+1] = temp
  				replace_count+=1
  	print('количество сравнений: ',compare_count,'\n','количество перестановок: ',replace_count)
def insertionSort(list_):
    compare_count = 0
    replace_count = 0
    for i in range(1, len(list_)):
        key = list_[i]
        j = i-1
        while j >= 0 and key < list_[j]:
        	compare_count+=1
        	list_[j + 1] = list_[j]
        	replace_count+=1
        	j -= 1

        list_[j + 1] = key
        replace_count+=1
    print('количество сравнений: ',compare_count,'\n','количество перестановок: ',replace_count)
def print_statistic_list(list_dub,method_sort):
	print("ИСХОДНЫЕ ДАННЫЕ:")
	print(list_dub,'\n')
	print('СОРТИРОВКА:')
	method_sort(list_dub)
	print(list_dub,'\n')
	print('СОРТИРОВКА ОТСОРТИРОВАННОГО МАССИВА:')
	method_sort(list_dub)
	print(list_dub,'\n')
	print('ПЕРЕВОРАЧИВАЕМ ИСХОДНЫЙ МАССИВ:')
	list_vr =list(list_[::-1])
	print(list_vr,'\n')
	print('СОРТИРУЕМ ИСХОДНЫЙ ПЕРЕВЕРНУТЫЙ МАССИВ:')
	method_sort(list_vr)
	print(list_,'\n')
	print('\n')


print('\t\t\tСОРТИРОВКА ПУЗЫРЬКОМ\t\t\t')
print('\t\t\t\t\t\tСОРТИРОВКА НА 40\t\t\t\t\t\t')
print_statistic_list(list_1,bubbleSort)
print('\t\t\t\t\t\tСОКРАЩАЕМ ИСХОДНЫЙ МАССИВ ДО 20\t\t\t\t\t\t:')
len_list_=int((len(list_)/2))
list_1 = list(list_[:len_list_])
print_statistic_list(list_1,bubbleSort)
print('\t\t\t\t\t\tСОКРАЩАЕМ ИСХОДНЫЙ МАССИВ ДО 10\t\t\t\t\t\t')
len_list_=int((len(list_)/2))
list_1 = list(list_[:len_list_])
print_statistic_list(list_1,bubbleSort)

print('\t\t\tСОРТИРОВКА ВСТАВКАМИ\t\t\t')
print('\t\t\t\t\t\tСОРТИРОВКА НА 40\t\t\t\t\t\t')
print_statistic_list(list_2,insertionSort)
print('\t\t\t\t\t\tСОКРАЩАЕМ ИСХОДНЫЙ МАССИВ ДО 20\t\t\t\t\t\t:')
len_list_=int(len(list_)/2)
list_2 = list(list_[:len_list_])
print_statistic_list(list_2,insertionSort)
print('\t\t\t\t\t\tСОКРАЩАЕМ ИСХОДНЫЙ МАССИВ ДО 10\t\t\t\t\t\t')
len_list_=int(len(list_)/2)
list_2 = list(list_[:len_list_])
print_statistic_list(list_2,insertionSort)
