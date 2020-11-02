# Merge Sort
# merge sort reference: https://www.geeksforgeeks.org/merge-sort/
import random
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

def merge_sort(values):
    if len(values) > 1:
        middle = len(values)//2
        left = values[:middle]
        right = values[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
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

def insert_sort(values):
    for i in range(1, len(values)):
        j = i - 1
        while values[i] < values[j]: 
            if j < 0 :
                break
            values[i], values[j] = values[j],values[i]
            i = j
            j = j-1
    return values

# testing input
# a = [12, 11, 13, 5, 6, 7]
time_list = []
compare_list = []

start = 0
end = 0
num = 0
output = 0

merge_spend_time = 0
insert_spend_time = 0

total_merge_time = []
total_insert_time = []

generated_list = []
count = 0
while count < 30:
    merge_time_list = []
    insert_time_list = []
    while len(generated_list) < 100:
        n = random.randint(0, 20)
        generated_list.append(n)

        new_gen1 = generated_list.copy()
        new_gen2 = generated_list.copy()

        merge_start_time = time.time()
        merge_sort_value = merge_sort(new_gen1)
        merge_end_time = time.time()

        insert_start_time = time.time()
        insert_sort_value = insert_sort(new_gen2)
        insert_end_time = time.time()

        merge_spend_time = merge_end_time-merge_start_time
        insert_spend_time = insert_end_time-insert_start_time
        merge_time_list.append(merge_spend_time)
        insert_time_list.append(insert_spend_time)

        if merge_spend_time > insert_spend_time:
            compare_list.append("insert")
        else:
            compare_list.append("merge")
    total_merge_time.append(merge_time_list)
    total_insert_time.append(insert_time_list)
    generated_list = []
    count += 1

merge_time_array = np.array(total_merge_time)
insert_time_array = np.array(total_insert_time)
y1_list = list(np.mean(merge_time_array,axis=0))# merge sort
y2_list = list(np.mean(insert_time_array,axis=0))# insert sort

x_list = [x for x in range(100)]
# y1_list = [y1 for y1 in merge_time_list] 
# y2_list = [y2 for y2 in insert_time_list] 

x_major_locator=MultipleLocator(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x_list, y1_list, color='r', linewidth=1, alpha=0.6)# merge sort
ax.plot(x_list, y2_list, color='b', linewidth=1, alpha=0.6)# insert sort
plt.savefig('/VL/space/zhan1624/CV_homework/algorithm_homework/output_image/merge_insert.png')