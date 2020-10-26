
def heapify(element, input_heap, fn=lambda x: x):
   
    input_heap.append(element)
    index = len(input_heap)-1

    while True:
        parent = int((index-1)/2)
        if fn(element) >= fn(input_heap[parent]):
            break
        
        else:
            input_heap[parent],input_heap[index] = input_heap[index],input_heap[parent]
            index = parent

    
def poll(input_heap, fn=lambda x: x):
    input_heap[0] = input_heap[-1]
    del input_heap[-1]
    final_length = len(input_heap)
    index = 0
    while True:
        parent = index
        left = parent * 2 + 1
        right = parent * 2 + 2
        if left >= final_length:
            break
        if left == final_length-1 and fn(input_heap[parent]) > fn(input_heap[left]):
            input_heap[parent],input_heap[left] = input_heap[left], input_heap[parent]
        elif fn(input_heap[parent]) > fn(input_heap[left]) and fn(input_heap[left]) < fn(input_heap[right]):
            input_heap[parent],input_heap[left] = input_heap[left], input_heap[parent]
            index = left
        elif fn(input_heap[parent]) > fn(input_heap[right]) and fn(input_heap[left]) > fn(input_heap[right]):
            input_heap[parent],input_heap[right] = input_heap[right], input_heap[parent]
            index = right

        



input_heap = [(1,4),(2,7),(3,5),(4,8),(5,9)]
#test_heap = [4,7,5,8,9]

#heapify((3,3), input_heap, fn=lambda x:x[1])
sinkup(input_heap, fn=lambda x: x[1])
print('quan')