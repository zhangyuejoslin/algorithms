def identifying(input_num, best_num):
    input_num.sort(reverse = True)
    return input_num


def deploying(input_list, list_length, agent_num):
    agent_dict = {}
    result = 0
    if list_length ==  agent_num:
        return sum(input_list)
    else:
        input_list.sort(reverse=True)

        for each_num in range(agent_num):
            agent_dict[each_num] = []
        
        for input_id, each_input in enumerate(input_list):
            fetch_id = input_id % agent_num
            agent_dict[fetch_id].append(each_input)

        for agent_key, agent_value in agent_dict.items():
            tmp_result = 0
            for value_id, value in enumerate(agent_value):
                tmp_result += value * (value_id+1)
            result += tmp_result
    return result


def genetic(input_num, input_list, tmp_list):
    input_list.sort()
    reversed_sorted_list = input_list[::-1]
    diff_list = []
    if tmp_list == input_list:
        return (True, None, None)
    elif tmp_list == reversed_sorted_list:
        return (True, 1, len(tmp_list))
    else:
        for input_id, each_input in enumerate(tmp_list):
            if each_input != input_list[input_id]:
                diff_list.append(input_id)
    position1 = diff_list[0]
    position2 = diff_list[-1]
    output_list1 = tmp_list[:position1] + [tmp_list[position2]] + tmp_list[position1+1:position2] + [tmp_list[position1]] + tmp_list[position2+1:]
    if output_list1 == input_list:
        return (1, position1+1, position2+1)
    else:
        output_list2 = tmp_list[:position1] + tmp_list[position1:position2+1][::-1] + tmp_list[position2+1:]
        if output_list2 == input_list:
            return (2, position1+1, position2+1)
        else:
            return (False, None, None)


def takedown(total_num, explore_num, explore_list):
    tmp_list = []
    if total_num == explore_num:
        return 0
    else:
        explore_list.sort()
        for explore_id, each_explore in enumerate(explore_list):
            if explore_id <= len(explore_list)-2:
                diff = explore_list[explore_id+1] - explore_list[explore_id]
                tmp_list.append(int(diff/2))
    if explore_list[0] != 0 :
        tmp_list.insert(0, explore_list[0])
    if explore_list[-1] != len(explore_list)-1:
        tmp_list.append(total_num-1-explore_list[-1])
    
    if not tmp_list:
        if total_num-1 - explore_list[0]> explore_list[0]:
            tmp_list.append(total_num)
        else:
            tmp_list.append(0)
    
    return max(tmp_list)
        
        


def thick(input_list):
    num1 = int(input_list[0])
    num2 = int(input_list[num1+1])
    
    list1 = input_list[1:num1+1]
    list2 = input_list[-num2:]

    result = 0
    for each_element in list1:
        if each_element in list2:
            result+=1
    return result


def guess(N, P, possible_colors, view):
    possibility_dict = {}
    for each_view in view:
        if each_view not in possibility_dict.keys():
            possibility_dict[each_view] = 1
        
        else:
            possibility_dict[each_view] += 1
    
    result= max(possibility_dict,key=lambda x:possibility_dict[x])
        
    print(result)



if __name__ == "__main__":
   
   # identifying
    # test_list1 = [6,7,11,6,17]
    # test_list2 = [7,3,19,5,3,11,13,10,3,6]
    # best_num_list = identifying(test_list2, 3)
    # for each_num in best_num_list[:3]:
    #     print(each_num)
    # print('quan')

    #deployting
    '''
    #input_list1 = [6, 1, 28, 10, 15, 3, 21]
    input_list2 = [2, 5, 6]
    input_num = 3
    agent_num = 3
    result = deploying(input_list2, input_num, agent_num)
    # print('quan')
    # num1, num2  =  tuple(map(int, input().split()))
    # input_list = list(map(int, input().split()))
    # result = deploying(input_list, num1, num2)
    # print(result)
    '''

    
    #genertic
    '''
    input_num = 100
    input_list = [4104, 8529, 49984, 54956, 63034, 82534, 84473, 86411, 92941, 95929, 108831, 894947, 125082, 137123, 137276, 142534, 149840, 154703, 174744, 180537, 207563, 221088, 223069, 231982, 249517, 252211, 255192, 260283, 261543, 262406, 270616, 274600, 274709, 283838, 289532, 295589, 310856, 314991, 322201, 339198, 343271, 383392, 385869, 389367, 403468, 441925, 444543, 454300, 455366, 469896, 478627, 479055, 484516, 499114, 512738, 543943, 552836, 560153, 578730, 579688, 591631, 594436, 606033, 613146, 621500, 627475, 631582, 643754, 658309, 666435, 667186, 671190, 674741, 685292, 702340, 705383, 722375, 722776, 726812, 748441, 790023, 795574, 797416, 813164, 813248, 827778, 839998, 843708, 851728, 857147, 860454, 861956, 864994, 868755, 116375, 911042, 912634, 914500, 920825, 979477]
    tmp_list = [4104, 8529, 49984, 54956, 63034, 82534, 84473, 86411, 92941, 95929, 108831, 894947, 125082, 137123, 137276, 142534, 149840, 154703, 174744, 180537, 207563, 221088, 223069, 231982, 249517, 252211, 255192, 260283, 261543, 262406, 270616, 274600, 274709, 283838, 289532, 295589, 310856, 314991, 322201, 339198, 343271, 383392, 385869, 389367, 403468, 441925, 444543, 454300, 455366, 469896, 478627, 479055, 484516, 499114, 512738, 543943, 552836, 560153, 578730, 579688, 591631, 594436, 606033, 613146, 621500, 627475, 631582, 643754, 658309, 666435, 667186, 671190, 674741, 685292, 702340, 705383, 722375, 722776, 726812, 748441, 790023, 795574, 797416, 813164, 813248, 827778, 839998, 843708, 851728, 857147, 860454, 861956, 864994, 868755, 116375, 911042, 912634, 914500, 920825, 979477]
    #input_list = [1, 5, 4, 3, 2, 6]
    #tmp_list = [1, 5, 4, 3, 2, 6]
    #tmp_list = [20, 30, 42, 60]
    #input_list = [20, 30, 42, 60]
    # tmp_list = [3,1,2]
    # input_list = [3,1,2]
    # input_num = int(input())
    # input_string = input()
    input_string = "4104 8529 49984 54956 63034 82534 84473 86411 92941 95929 108831 894947 125082 137123 137276 142534 149840 154703 174744 180537 207563 221088 223069 231982 249517 252211 255192 260283 261543 262406 270616 274600 274709 283838 289532 295589 310856 314991 322201 339198 343271 383392 385869 389367 403468 441925 444543 454300 455366 469896 478627 479055 484516 499114 512738 543943 552836 560153 578730 579688 591631 594436 606033 613146 621500 627475 631582 643754 658309 666435 667186 671190 674741 685292 702340 705383 722375 722776 726812 748441 790023 795574 797416 813164 813248 827778 839998 843708 851728 857147 860454 861956 864994 868755 116375 911042 912634 914500 920825 979477"
    input_list = []
    tmp_list = []
    for each_input in input_string.split():
        input_list.append(each_input)
        tmp_list.append(each_input)
    flag, element1, element2 = genetic(input_num, input_list, tmp_list)
    if not flag:
        print('no')
    else:
        if not element1 and not element2:
            print('yes')
        else:
            if flag == 1:
                print('yes')      
                print(" ".join(("swap", str(element1), str(element2))))
            elif flag == 2:
                print('yes')      
                print(" ".join(("reverse", str(element1), str(element2))))
    '''

    
    #list1 = [4, 76, 16, 71, 56, 7, 77, 31, 2, 66, 12, 32, 57, 11, 19, 14, 42]
    #list2 = [13, 1, 11, 10, 6]
    list3 = [13]
    takedown(20, 1, list3)
    # num1, num2 = tuple(map(int, input().split())))

    # input_list = list(map(int, input().split))

    # result = takedown(num1, num2, input_list)
    #print(result)
    

    #thick
    '''
    #input_list = ["6", "a", "b", "c", "d", "e", "f", "4", "f", "b", "c", "o"]
    # input_list = ["5","asfsf34","sahsdg2","ln2hr4r","fhdsd42","325sdd3","3","sahsdg2","fjfdry4","sdgnjl5"]
    # thick(input_list)
    input_list = []
    num1 = int(input())
    for _ in range(num1):
        input_list.append(input())
    num2 = int(input())
    input_list.append(num2)
    for _ in range(num2):
        input_list.append(input())
    result = thick(input_list)
    print(result)
    '''
    # list1 = ["gainsboro", "orange_peel", "fawn", "yellow", "white_smoke"]
    # list2 = ["orange_peel", "orange_peel", "gainsboro", "yellow"]
    # guess(5, 0, list1, list2)