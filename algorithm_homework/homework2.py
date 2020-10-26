def satellite(num, input_list):
    index_list = [id for id, (s1,s2) in enumerate(input_list) if s1-s2 >0]
    for each_index in index_list:
        total_num = 0
        tmp_index = input_list[each_index:]+input_list[0:each_index]
        tmp_index = [s1-s2 for s1, s2 in tmp_index]
        for t_i in tmp_index:
            total_num += t_i
            if total_num < 0:
                break
        if total_num >= 0:
            return each_index


def satellite2(num, input_list):
    index_list = [s1-s2 for s1,s2 in input_list]
    flipped_add_index = []
    total_num = 0
    for index_id, each_index in enumerate(index_list[::-1]):
        total_num += each_index
        flipped_add_index.append(total_num)

    new_index = flipped_add_index[::-1]
    return new_index.index(max(new_index))


def tracking_frequency(input_num, num_list):
    result_dict = {}
    max_total = 0
    max_num = 0
    
    for num in num_list:
        if num not in result_dict.keys():
            result_dict[num] = 1
        else:
            result_dict[num] += 1
        if result_dict[num] > max_total:
            max_total = result_dict[num]
            max_num = num
        

    return max_num  


def tracking_target(input_num, action_list):
    def search(element, sorted_input_list, start, end):
        middle = int((start+end)/2)
        if element > sorted_input_list[middle]:
            if start == middle:
                return end
            return search(element, sorted_input_list,middle,end)
        elif element < sorted_input_list[middle]:
            if start == middle:
                return start
            return search(element, sorted_input_list,start, middle)
        else:
            return middle
    
    def search2(element, sorted_input_list, start, end):
        middle = int((start+end)/2)
        while True:
            if element > sorted_input_list[middle]:
                if start == middle:
                    return end
                start = middle
                middle = int((start+end)/2)
            elif element < sorted_input_list[middle]:
                if start == middle:
                    return start
                end = middle
                middle = int((start+end)/2)
            else:
                return middle
    
    
    current_list = []
    output_list = []
    order_list =[] 
    for value in action_list:
        if value[0] == 1:
            current_list.append(value[1])
            if not order_list:
                order_list.append(value[1])
            else:
                insert_position = search2(value[1], order_list, 0, len(order_list))
                order_list.insert(insert_position,value[1])
        elif value[0] == 2:
            remove_value = current_list[-1]
            current_list = current_list[0:len(current_list)-1]    
            remove_position =  search2(remove_value, order_list, 0, len(order_list))
            del order_list[remove_position]
        else:
            output_list.append(order_list[-1])

    return output_list


def blending(num, input_list):
    def search(element, sorted_input_list, start, end, fn=lambda x: x):
        middle = int((start+end)/2)
        while True:
            if element > sorted_input_list[middle]:
                if start == middle:
                    return end
                start = middle
                middle = int((start+end)/2)
            elif element < sorted_input_list[middle]:
                if start == middle:
                    return start
                end = middle
                middle = int((start+end)/2)
            else:
                return middle
    
    def get_median(sorted_list):
        length = len(sorted_list)
        if length == 1:
            return sorted_list[0]
        middle = int(length/2)
        if length%2 == 0:
            return (sorted_list[middle] +sorted_list[middle-1])/2
        else:
            return sorted_list[middle]
    
    current_list = []
    output_list = []
    order_list = []
    for action, value in input_list:  
        value = int(value)  
        if action == "a":
            current_list.append(value)
            if not order_list:
                order_list.append(value)
                output_list.append(value)
            else:
                insert_position = search(value, order_list, 0, len(order_list))
                order_list.insert(insert_position,value)
                output_list.append(get_median(order_list))
        
        elif action == "r":
            if not current_list:
                output_list.append('Wrong!')
            else:
                remove_position = search(value, order_list, 0, len(order_list))
                if value > order_list[-1] or value < order_list[0]:
                    output_list.append('Wrong!')
                    continue
                # if remove_position > len(order_list)-1:
                #     output_list.append('Wrong!')
                #     continue
                # if value != order_list[remove_position]:
                #     output_list.append('Wrong!')
                #     continue
             
                tmp_current_list = current_list[::-1]              
                tmp_current_list.remove(value)
                current_list = tmp_current_list[::-1]
                order_list = order_list[0:remove_position]+ order_list[remove_position+1:len(order_list)]
                
               

                if order_list:
                    output_list.append(get_median(order_list))
                else:
                    output_list.append('Wrong!')
                
                
    
    return output_list


def crack(num, input_list):
    def search(element, sorted_input_list, start, end, fn=lambda x: x):
        if not sorted_input_list:
            return 0
        middle = int((start+end)/2)
        if fn(element) > fn(sorted_input_list[middle]):
            if start == middle:
                return end
            return search(element, sorted_input_list,middle, end, fn)
        elif fn(element) < fn(sorted_input_list[middle]):
            if start == middle:
                return start
            return search(element, sorted_input_list,start, middle, fn)
        else:
            return middle
    
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
            if left == final_length-1:
                if fn(input_heap[parent]) > fn(input_heap[left]):
                    input_heap[parent],input_heap[left] = input_heap[left], input_heap[parent]
                else:
                    break
            elif fn(input_heap[parent]) > fn(input_heap[left]) and fn(input_heap[left]) < fn(input_heap[right]):
                input_heap[parent],input_heap[left] = input_heap[left], input_heap[parent]
                index = left
            elif fn(input_heap[parent]) > fn(input_heap[right]) and fn(input_heap[left]) > fn(input_heap[right]):
                input_heap[parent],input_heap[right] = input_heap[right], input_heap[parent]
                index = right
    
    

    
    ordered_list = []
    output_list = []
    for each_time_tuple in input_list:
        heapify(each_time_tuple, ordered_list,fn=lambda x:x[0])
        
       

    tmp_list = []
    current_time = 0
    while True:
        if not tmp_list and not ordered_list:
            break

        while ordered_list:
            time1,time2 = ordered_list[0]
            if time1 <= current_time:
                poll(ordered_list, fn=lambda x:x[0])
                heapify((time1,time2),tmp_list, fn=lambda x:x[1])
            else:
                break      

        if not tmp_list:
            tmp_list.append(ordered_list[0])
            current_time = ordered_list[0][0]
            poll(ordered_list, fn=lambda x:x[0])

        current_time += tmp_list[0][1]
        output_list.append(current_time - tmp_list[0][0])
        poll(tmp_list,fn=lambda x: x[1])
    
    return int(sum(output_list)/num)






if __name__ == "__main__":
    '''
    for satellite
    #input_list = [(1,5),(10,3),(3,4)]
    #input_list = [(1,11),(2, 12),(3, 13),(4, 14),(5, 15),(6, 16),(7, 17),(8, 18),(9, 19),(10, 20),(11, 1),(12, 2),(13, 3),(14, 4),(15, 5),(16, 6),(17, 7),(18, 8),(19, 9),(20, 10)]
    input_list = [(5, 15),(16, 6),(2, 12),(3, 13),(14, 4),(7, 17),(1, 11),(13, 3),(20,10),(15, 5),(6, 16),(4, 14),(9, 19),(11, 1),(8, 18),(17, 7),(18, 8),(12, 2),(10, 20),(19, 9)]

    out_index = satellite2(20,input_list)
    '''

    '''
    for frequency
    input_list = [63,63,63,8,3,8,63,3]
    #input_list = [97,97,29,68,68,97,97,83,97,68,29,97,68,83,83]
    result = tracking(18, input_list)
    '''

    '''
    for tracking target
    input_list = [(1, 97),(2,),(1, 20),(2,),(1, 26),(1, 20),(2,),(3,),(1, 91),(3,)]
    #input_list = [(1,83),(3,),(2,),(1,76)]
    tracking_target(10, input_list)
    '''
    
    '''
    #input_list = [("r",1),("a",1),("a",2),("a",1),("r",1),("r",2),("r",1)]
    out_put_list = blending(7, input_list)
    '''

    #input_list = [(2, 5), (11,2),(1000,12),(10,10)]
    #input_list = [(0, 3), (1, 9),(2, 6)]
    # input_list = [(961148050, 385599125),(951133776, 376367013),(283280121, 782916802),(317664929, 898415172),(980913391, 847912645)]
    #output = crack(3, input_list)
    # num = input()
    # input_list = []
    # for _ in range(int(num)):
    #     input_list.append(tuple(map(int, input().rstrip().split())))

    # result = crack(num, input_list)
    # print(result)
 


       