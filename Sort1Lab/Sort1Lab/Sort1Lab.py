import matplotlib.pyplot as plt
import random
import numpy as np
import sys
import threading
import time
import sys


def writer(arr_from_file, Name):    
    g = open(Name + str(len(arr_from_file)) + ".txt", "w")
    g.write(", ".join(arr_from_file))
    g.close()
    


def my_dec(func):
    def sort(arr_from_file):
        arr_from_file = [int(item) for item in arr_from_file]
        start = time.time()
        func(arr_from_file)
        end = time.time()        
        return end - start

    return sort


@my_dec
def bublesort(arr_from_file):
    for i in range(len(arr_from_file)- 1):
         for j in range(len(arr_from_file)-i-1):
             if (arr_from_file)[j] > (arr_from_file)[j+1]:
                (arr_from_file)[j], (arr_from_file)[j+1] = (arr_from_file)[j+1], (arr_from_file)[j]
    arr_from_file= [str(item) for item in arr_from_file]
    Name = sys._getframe().f_code.co_name
    writer(arr_from_file, Name)
    
    
def draw(size, timer, timer2):
    fig = plt.figure()
    xt, yt, yt2 = max(size), max(timer), max(timer2)
    plt.text(xt,yt2,"Сортировка расческой")
    plt.text(xt,yt,"Пузырьковая сортировка")
    plt.xlabel("Кол-во элементов в текстовом файле")
    plt.ylabel("Время в секундах")
    plt.title("Cравнение затрат времени в зависимости от кол-ва элементов")
    x = np.array([a for a in size])
    y = np.array([a for a in timer])
    y2 = np.array([a for a in timer2])
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()

@my_dec
def comb_sort(arr_from_file):
    for i in range(1, len(arr_from_file)):
        temp = arr_from_file[i]
        j = i - 1
        while (j >= 0 and temp < arr_from_file[j]):
            arr_from_file[j + 1] = arr_from_file[j]
            j = j - 1
        arr_from_file[j + 1] = temp
   
    
    arr_from_file= [str(item) for item in arr_from_file]
    Name = sys._getframe().f_code.co_name
    writer(arr_from_file, Name)

def fileRead(file_name):
    return open(file_name, "r").read().split(', ')

def main():
    size = []
    timer = []
    timer2 =[]
    for i in range(5):
        file_name = "Test" + str(i) + ".txt"
        arr_from_file = fileRead(file_name)
        size.append(len(arr_from_file))         
        t1 = threading.Thread(target=timer.append(bublesort(arr_from_file)))
        t2 = threading.Thread(target=timer2.append(comb_sort(arr_from_file)))        
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    draw(size, timer, timer2)
    

if __name__ =="__main__":
    main()




