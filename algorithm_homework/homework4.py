# Merge Sort
# merge sort reference: https://www.geeksforgeeks.org/merge-sort/
import random
import time

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
a = [12, 11, 13, 5, 6, 7]
time_list = []
compare_list = []

start = 0
end = 1
num = 0

merge_spend_time = 0
insert_spend_time = 0


while True:
    if merge_spend_time <= insert_spend_time and merge_spend_time >0  and insert_spend_time>0:
        break
    generated_list = []
    for each_i in range(start, end):
        n = random.randint(0, 10)
        generated_list.append(n)
        
    merge_start_time = time.time()
    merge_sort_value = merge_sort(generated_list)
    merge_end_time = time.time()

    insert_start_time = time.time()
    insert_sort_value = insert_sort(generated_list)
    insert_end_time = time.time()

    merge_spend_time = merge_end_time-merge_start_time
    insert_spend_time = insert_end_time-insert_start_time

    time_list.append((merge_spend_time, insert_spend_time))
    if merge_spend_time > insert_spend_time:
        compare_list.append("insert")
    else:
        compare_list.append("merge")
    end += 1 
  
print(end)


