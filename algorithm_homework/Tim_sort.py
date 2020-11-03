import random
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

def merge_sort(left, right):
    values = []
    while len(left)>0  and len(right)>0:
        if left[0] < right[0]:
            values.append(left[0])
            left.pop(0)
        else:
            values.append(right[0])
            right.pop(0)
    # to apend the rest values 
    for i in left:
        values.append(i)
    for j in right:
        values.append(j)

    return values

def timsort(array, partition_k):
    min_run = partition_k
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge_sort(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array
        size *= 2

    return array

def merge_sort1(values):
    if len(values) > 1:
        middle = len(values)//2
        left = values[:middle]
        right = values[middle:]
        left = merge_sort1(left)
        right = merge_sort1(right)
        values = []
    
        while len(left)>0  and len(right)>0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)
        # to apend the rest values 
        for i in left:
            values.append(i)
        for j in right:
            values.append(j)

    return values

def insert_sort1(values):
    for i in range(1, len(values)):
        j = i - 1
        while values[i] < values[j]: 
            if j < 0 :
                break
            values[i], values[j] = values[j],values[i]
            i = j
            j = j-1
    return values


generated_list = []

start = 0
end = 100
partition_k = 2
partition_end = end
spend_all = []
count = 0
partition_list = []

check_hybrid_K_N = False # The first experiment to check relation between k and n

merge_start_time = 0
merge_end_time = 0
merge_time = 0

insertion_start_time = 0
insertion_end_time = 0
insertion_time = 0

hybrid_start_time = 0
hybrid_end_time = 0
hybrid_time = 0

hybrid_list = []
merge_list = []
insertion_list = []

if check_hybrid_K_N:

    while count<30:
        spend_time_list = []
        generated_list = []
        for each_i in range(start, end):
            n = random.randint(0, 100)
            generated_list.append(n)

        while partition_k <= partition_end:
            new_list = generated_list.copy()
            start_time = time.time()
            timsort(new_list, partition_k)
            end_time = time.time()
            if len(partition_list) < end-1:
                partition_list.append(partition_k)
            spend_time_list.append((end_time - start_time))
            partition_k +=1
        spend_all.append(spend_time_list)
        count += 1
        partition_k = 2
        
    hybrid_array = np.array(spend_all)
    hybrid_list = list(np.mean(hybrid_array,axis=0))# hybrid sort

    x_list = [x for x in partition_list]
    y_list = [y for y in hybrid_list]
    x_major_locator=MultipleLocator(30)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.set_xlabel('k')
    ax.set_ylabel('y')
    ax.plot(x_list, y_list, color='r', linewidth=1, alpha=0.6)
    plt.savefig('/VL/space/zhan1624/CV_homework/algorithm_homework/output_image/timsort_300.png')


else: # the second experiment to compare hybrid sort with merge and insertion sort. K = 16
    while count < 30:
        generated_list = []
        each_hybrid_list = []
        each_merge_list = []
        each_insertion_list = []
        while len(generated_list) < 100:
            n = random.randint(0, 20)
            generated_list.append(n)

            new_list1 = generated_list.copy()
            new_list2 = generated_list.copy()
            new_list3 = generated_list.copy()

            hybrid_start_time = time.time()
            timsort(new_list1,16)
            hybrid_end_time = time.time()
            hybrid_time = hybrid_start_time -hybrid_end_time
            each_hybrid_list.append(hybrid_time)

            merge_start_time = time.time()
            merge_sort1(new_list2)
            merge_end_time = time.time()
            merge_time = merge_end_time - merge_start_time
            each_merge_list.append(merge_time)

            insertion_start_time = time.time()
            insert_sort1(new_list3)
            insertion_end_time = time.time()
            insertion_time = insertion_end_time - insertion_start_time
            each_insertion_list.append(insertion_time)

        hybrid_list.append(each_hybrid_list)
        merge_list.append(each_merge_list)
        insertion_list.append(each_insertion_list)
        count += 1

    hybrid_list = np.mean(np.array(hybrid_list), axis=0)
    merge_list = np.mean(np.array(merge_list),axis=0)
    insertion_list = np.mean(np.array(insertion_list),axis=0)

 
    y_list_hybrid = [y1 for y1 in hybrid_list]
    y_list_merge = [y2 for y2 in merge_list]
    y_list_insertion = [y3 for y3 in insertion_list]
    x_list = [x for x in range(100)]

    x_major_locator=MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot(x_list, y_list_hybrid, color='r', linewidth=1, alpha=0.6, label="hybrid")
    ax.plot(x_list, y_list_merge, color='b', linewidth=1, alpha=0.6, label="merge")
    ax.plot(x_list, y_list_insertion, color='g', linewidth=1, alpha=0.6,label="insertion")
    plt.savefig('/VL/space/zhan1624/CV_homework/algorithm_homework/output_image/comparision.png')




        


