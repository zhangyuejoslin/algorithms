# def climb(n,m,c):
#     final_result = 0
#     tmp_left = int(n/m)
#     while True:
#         combine_left = tmp_left/c
#         if combine_left < 1.0:
#             break
#         elif combine_left == 1.0:
#             final_result += 1
#             break
#         else:
#             generate_num = int(combine_left)
#             tmp_left = generate_num + (tmp_left-generate_num*c)
#             final_result += generate_num

#     final_result += int(n/m)
#     return final_result

# def poker(s,k):
#     def boundary_check(s):
#         return s%1000000

#     for i in range(k):
#         if s % 2 == 0:
#             s = s - 99
#             s = boundary_check(s)
#             s = 3 * s
#             s = boundary_check(s)
#         else:
#             s = s - 15
#             s = boundary_check(s)
#             s = 2 * s
#             s = boundary_check(s)
#     return s

    
# def lift(input_list):
#     def positive(input):
#         if input < 0:
#             input = 0
#         return input

#     def get_min_num(input_list):
#         positive_list = []
#         left_num = 0
#         for each_input in input_list:
#             if each_input > 0:
#                 left_num += 1
#                 positive_list.append(each_input)
#         return left_num, min(positive_list)

#     result = []
#     min_num = 0
#     while True:
#         left_num, min_num = get_min_num(input_list)
#         input_list = [positive(each_input-min_num) for each_input in input_list]    
        
#         result.append(left_num)
#         if not any(input_list):
#             break
#     return result


# import math
# def minerva_num(min_num, max_num):
#     def is_dive_twelve(input_num):
#         return input_num % 12 == 0

#     def is_sqr(input_num):
#         tmp_sqrt_num = int(math.sqrt(input_num))
#         return tmp_sqrt_num ** 2 == input_num



#     twelve_num = 0
#     sqrt_num = 0
#     both_t_s = 0
    
#     twelve_min_num = int(min_num / 12)
#     twelve_max_num = int(max_num / 12)
#     twelve_num = twelve_max_num - twelve_min_num
#     if is_dive_twelve(min_num):
#         twelve_num +=1


#     sqrt_min_num = int(math.sqrt(min_num))
#     sqrt_max_num = int(math.sqrt(max_num))
#     sqrt_num = sqrt_max_num - sqrt_min_num
#     if is_sqr(min_num):
#         sqrt_num += 1
    
#     if sqrt_min_num ** 2 < min_num:
#         sqrt_min_num =sqrt_min_num +1
    

#     for each_sqrt in range(sqrt_min_num, sqrt_max_num+1):
#         if is_dive_twelve(each_sqrt**2):
#             both_t_s +=1
#     return twelve_num, sqrt_num, both_t_s

 # def overlap_check(start1, end1, start2, end2):
    #     if start1[0] <= end2[0] and end1[0]>=end2[0] and start2[1] <= end1[1] and end2[1]>= end1[1]:
    #         return True
    #     elif start2[0]>= end1[0] and end2[0] >= end1[0] and start1[1] <= end2[1] and end1[1]>=end2[1]:
    #         return True
    #     elif start1[0] == start2[0] and end1[0] == end2[0] and ((start1[1] <= start2[1] and end1[1]>start2[1]) or (start1[1] >= start2[1] and end2[1]>=start1[1])):
    #         return True
    #     elif start1[1] == start2[1] and end1[1] == end2[1] and ((start1[0] <= start2[0] and end1[0]>start2[0]) or (start1[0] >= start2[0] and end2[0]>=start1[0])):
    #         return True
    #     else:
    #         return False


# def stage(m, n, input_list):
#     total_matrix = []
#     tmp_result_list = []
#     final_result_list = []
#     num_G = 0
    
#     final_score = 0
#     for each_element in input_list:
#         tmp_list = []
#         for each_word in each_element:
#             tmp_list.append(each_word)
#         total_matrix.append(tmp_list)
    	
    
#     def matrix_id_check(id_tuple):
#         tmp_row_id, tmp_column_id = id_tuple
#         if tmp_row_id >=0 and tmp_row_id<m:
#             if tmp_column_id>=0 and tmp_column_id<n:
#                 return id_tuple
            

#     def pano_matrix(pano_row_id, pano_column_id, num):
#         left_id = (pano_row_id, pano_column_id-num)
#         upper_id = (pano_row_id-num, pano_column_id)
#         right_id = (pano_row_id, pano_column_id+num)
#         below_id = (pano_row_id+num, pano_column_id)
#         return matrix_id_check(left_id), matrix_id_check(upper_id), matrix_id_check(right_id), matrix_id_check(below_id)

#     def overlap_check(tuple1, tuple2):
#         position1 = []
#         position2 = []
#         num1, center1, left1, upper1, right1, below1 = tuple1
#         num2, center2, left2, upper2, right2, below2 = tuple2
#         max_num = max(num1, num2)
#         if center1 == center2:
#             return True
#         else:
#             for each_x1 in range(left1[1], right1[1]+1):
#                 position1.append((left1[0], each_x1))
#             for each_y1 in range(upper1[0], below1[0]+1):
#                 position1.append((each_y1, upper1[1]))
            
#             for each_x2 in range(left2[1], right2[1]+1):
#                 position2.append((left2[0], each_x2))
#             for each_y2 in range(upper2[0], below2[0]+1):
#                 position2.append((each_y2, upper2[1]))
            
#             if list(set(position1).intersection(set(position2))):
#                 return True
#             else:
#                 return False


#     for row_id, each_row in enumerate(total_matrix):
#         for column_id, each_column in enumerate(each_row):
#             left_id, upper_id, right_id, below_id = pano_matrix(row_id, column_id, 1)  
#             if each_column == "G":
#                 num_G += 1
#             if left_id and upper_id and right_id and below_id:
#                 if total_matrix[left_id[0]][left_id[1]] == each_column and total_matrix[upper_id[0]][upper_id[1]] == each_column \
#                 and total_matrix[right_id[0]][right_id[1]] == each_column and total_matrix[below_id[0]][below_id[1]] == each_column and each_column=="G":
#                     tmp_result_list.append((1,(row_id,column_id), left_id, upper_id, right_id, below_id))  
                            
#                     num = 2           
#                     while True:
#                         new_left_id, new_upper_id, new_right_id, new_below_id = pano_matrix(row_id, column_id, num)
#                         if new_left_id and new_upper_id and new_right_id and new_below_id:
#                             if total_matrix[new_left_id[0]][new_left_id[1]] == each_column and total_matrix[new_upper_id[0]][new_upper_id[1]]== each_column and\
#                                 total_matrix[new_right_id[0]][new_right_id[1]]== each_column and total_matrix[new_below_id[0]][new_below_id[1]]== each_column:
#                                 tmp_result_list.append((num,(row_id,column_id),new_left_id, new_upper_id, new_right_id, new_below_id))          
                                  
#                                 num += 1
#                             else:
#                                 break
#                         else:
#                             break
                       
#     overlap_max_num = 0
#     if not tmp_result_list:
#         if num_G > 1:
#         	final_score = 1
#         else:
#             final_score = 0
#     elif len(tmp_result_list) == 1:
#          if num_G - tmp_result_list[0][0]*4+1 == 0
#         	final_score = 0
#         else:
#         	final_score = tmp_result_list[0][0]*4+1
#     else:
#         for first_id, first_each in enumerate(tmp_result_list):
#             for second_each in tmp_result_list[first_id+1:]:
#                 if overlap_check(first_each, second_each):
#                     if max(first_each[0],second_each[0]) > overlap_max_num:
#                         overlap_max_num = max(first_each[0],second_each[0])
#                     continue
#                 else:
#                     tmp_score = (first_each[0]*4+1) * (second_each[0]*4+1)
#                     final_result_list.append(tmp_score)

#         if not final_result_list:
#              final_result_list.append(overlap_max_num*4+1)

#         final_score = sorted(final_result_list, reverse=1)[0]


#     return final_score

# def rotation(m,n,matrix, rotate_nums):
   
#     all_circles = []
#     all_new_circles = []
#     final_result = []

#     def get_circles(input_matrix, degree): 
#         tmp_list1 = []
#         tmp_list2 = []
#         tmp_list3 = []
#         tmp_list4 = []
#         neg_index3 = -1
#         neg_index4 = -1
#         for row_id, each_row in enumerate(matrix): 
#             for column_id, each_column in enumerate(each_row):
#                 if row_id == degree and column_id >= degree and column_id < n-1-degree:             
#                     tmp_list1.append(each_column)
#                     continue
#                 if column_id == n-1-degree and row_id >= degree and row_id < m-1-degree:
#                     tmp_list2.append(each_column)
#                     continue
#                 if row_id == m-1-degree and column_id > degree and column_id <= n-1-degree:
#                     tmp_list3.insert(neg_index3, each_column)
#                     neg_index3 -= 1
#                     continue
#                 if column_id == degree and row_id > degree and row_id <= m-1-degree:
#                     tmp_list4.insert(neg_index4, each_column)
#                     neg_index4 -= 1
#                     continue
#         return get_rotate((tmp_list1 + tmp_list2 + tmp_list3 + tmp_list4),rotate_nums)
    
#     def get_rotate(input_list, rotate_nums):
#         for each_r in range(rotate_nums):
#             input_list.append(input_list[0])
#             input_list.pop(0)
#         return input_list
    
    
#     def get_compact(tmp_list, degree_m, degree_n):
#         new_compact_list = []
#         new_tmp_list1 = []
#         new_tmp_list2 = []
#         new_tmp_list3 = []
#         new_tmp_list4 = []
#         middle_tmp_list = []
#         forward = n
#         backward = -1
#         for t_id, each_t in enumerate(tmp_list):
#             if t_id >= 0 and t_id <= degree_n-1:
#                 new_tmp_list1.append(each_t)
#                 continue
#             if t_id >=degree_n-1 and t_id <= degree_m + degree_n-3:
#                 new_tmp_list2.append(each_t)        
#                 continue
#             if t_id >= degree_m + degree_n-3 and t_id <= degree_m+2*degree_n-3:
#                 new_tmp_list3.append(each_t)
#                 continue
#             if t_id >= 2*degree_n+degree_m-3 and t_id <= 2*degree_m+2*degree_n-4:
#                 new_tmp_list4.append(each_t)
#                 continue
#         new_tmp_list3 = new_tmp_list3[::-1]
#         new_tmp_list4 = new_tmp_list4[::-1]
#         middle_tmp_list = list(zip(*[new_tmp_list4,new_tmp_list2]))
#         middle_tmp_list = [list(each_m) for each_m in middle_tmp_list]
#         new_compact_list.append(new_tmp_list1)
#         if middle_tmp_list:
#             new_compact_list += middle_tmp_list
#         new_compact_list.append(new_tmp_list3)
#         return new_compact_list
    
#     def list_cross_combine(list1,list2):
#         c_list1_list2 = list1 + list2
#         c_list1_list2.append(c_list1_list2[1])
#         c_list1_list2.pop(1)
#         return c_list1_list2
            
#     def get_combination(circles_list):
#         for circle_id, each_circle in enumerate(circles_list[::-1]):
#             if circle_id == len(circles_list) - 1:
#                 break
#             next_circle = circles_list[::-1][circle_id+1][1:-1]
#             tmp_circle = list(zip(*[next_circle, each_circle]))
#             new_tmp_middle = []
#             for t_c in tmp_circle:
#                 t_c_1, t_c_2 = t_c
#                 new_tmp_middle.append(list_cross_combine(t_c_1, t_c_2))
#             circles_list[::-1][circle_id+1][1:-1] = new_tmp_middle
#         return circles_list


#     # if m == 3 or n == 3:
#     #     all_circles.append(get_circles(matrix , 0))


  
#     for each_circle_num in range(int(min(m,n)/2)):
#         all_circles.append(get_circles(matrix , each_circle_num))
    
#     tmp_m = m
#     tmp_n = n
#     for c_id, compact_num in enumerate(range(int(min(m,n)),0,-2)):
#         all_new_circles.append(get_compact(all_circles[c_id],tmp_m,tmp_n))
#         tmp_m -= 2
#         tmp_n -= 2

    
#     final_result = get_combination(all_new_circles)[0]

    
#     return final_result
    
    
  

        


#list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] # 442
# list2 = [[1,2,3,4],[7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]]#547
#list3 = [[1,2],[3,4]]


#list4 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]

# final_result = rotation(5,4,list2,7)
# final_result = list(zip(*final_result))
# for each_result in final_result:
#     print(*each_result)




#input_list = ['GGGGGG', 'GBBBGB','GGGGGG','GGBBGB','GGGGGG']
#input_list = ['BGBBGB','GGGGGG','BGBBGB','GGGGGG','BGBBGB','BGBBGB']
# input_list = ['GB',"BB"]
# num_row = 2
# num_column = 2

#input_list = ['GGGGGGGGG','GBBBGGBGG','GBBBGGBGG','GBBBGGBGG','GBBBGGBGG','GBBBGGBGG','GBBBGGBGG','GGGGGGGGGG']
#input_list = ['GBGBGGB','GBGBGGB','GBGBGGB','GGGGGGG','GGGGGGG','GBGBGGB','GBGBGGB']
#input_list = ['GGGGGGGGGG','GBBBBBBGGG','GGGGGGGGGG','GGGGGGGGGG','GBBBBBBGGG','GGGGGGGGGG','GBBBBBBGGG','GBBBBBBGGG','GGGGGGGGGG']
# input_list = ['GGGGGGGGGGGG','GBGGBBBBBBBG','GBGGBBBBBBBG','GGGGGGGGGGGG','GGGGGGGGGGGG','GGGGGGGGGGGG','GGGGGGGGGGGG',
# 'GBGGBBBBBBBG',
# 'GBGGBBBBBBBG',
# 'GBGGBBBBBBBG',
# 'GGGGGGGGGGGG',
# 'GBGGBBBBBBBG']






#input_list =['GGGGGGG','BGBBBBG','BGBBBBG','GGGGGGG','GGGGGGG','BGBBBBG']


#input_list = ['GBGBGGB','GBGBGGB','GBGBGGB','GGGGGGG','GGGGGGG','GBGBGGB','GBGBGGB']

# num_row,num_column = map(int, input().split())
# input_list =[]
# for column in range(num_row):
#     input_list.append(input())
# stage(num_row,num_column, input_list)



# Complete the targetRotation function below.
def targetRotation(m,n,matrix, rotate_nums):
    new_matrix = [[-1] * n for _ in range(m)]
    
    def get_circles(input_matrix, degree): 
        tmp_list1 = []
        tmp_list2 = []
        tmp_list3 = []
        tmp_list4 = []
        neg_index3 = -1
        neg_index4 = -1

        for row_id, each_row in enumerate(matrix): 
            for column_id, each_column in enumerate(each_row):
                if row_id == degree and column_id >= degree and column_id < n-1-degree:             
                    tmp_list1.append(each_column)
                    continue
                if column_id == n-1-degree and row_id >= degree and row_id < m-1-degree:
                    tmp_list2.append(each_column)
                    continue
                if row_id == m-1-degree and column_id > degree and column_id <= n-1-degree:
                    tmp_list3.insert(neg_index3, each_column)
                    neg_index3 -= 1
                    continue
                if column_id == degree and row_id > degree and row_id <= m-1-degree:
                    tmp_list4.insert(neg_index4, each_column)
                    neg_index4 -= 1
                    continue
        before_rotate = tmp_list1 + tmp_list2 + tmp_list3 + tmp_list4
        new_tmp_list = get_rotate(before_rotate,rotate_nums)
        seperate_id = (len(tmp_list1), len(tmp_list2), len(tmp_list3), len(tmp_list4))
      
        return new_tmp_list, seperate_id
    
    def get_rotate(input_list, rotate_nums):
        tmp_input = input_list
        rotate_nums = rotate_nums % len(input_list)
        if len(set(input_list)) == 1:
            return input_list
        else:
            input_list = tmp_input[rotate_nums:]
            input_list += tmp_input[0:rotate_nums]
            return input_list
    
    def get_compact(new_tmp_list, seperate_id, degree):
        length1, length2, length3, length4 = seperate_id
        new_tmp_list1 = new_tmp_list[0:length1]
        new_tmp_list2 = new_tmp_list[length1:length1+length2]
        new_tmp_list3 = new_tmp_list[length1+length2:length1+length2+length3]
        new_tmp_list4 = new_tmp_list[length1+length2+length3:length1+length2+length3+length4]
        new_tmp_list3 = new_tmp_list3[::-1]
        new_tmp_list4 = new_tmp_list4[::-1]

        for row_id, each_row in enumerate(new_matrix): 
            for column_id, each_column in enumerate(each_row):
                if row_id == degree and column_id >= degree and column_id < n-1-degree:             
                    new_matrix[row_id][column_id] = new_tmp_list1[column_id-degree]
                    continue
                if column_id == n-1-degree and row_id >= degree and row_id < m-1-degree:
                    new_matrix[row_id][column_id] = new_tmp_list2[row_id-degree]
                    continue
                if row_id == m-1-degree and column_id > degree and column_id <= n-1-degree:
                    new_matrix[row_id][column_id] = new_tmp_list3[column_id-degree-1] 
                    continue
                if column_id == degree and row_id > degree and row_id <= m-1-degree:
                    new_matrix[row_id][column_id] = new_tmp_list4[row_id-degree-1]
                    continue
          
    for each_circle_num in range(int(min(m,n)/2)):
        new_circle, edge_id = get_circles(matrix , each_circle_num)
        get_compact(new_circle, edge_id, each_circle_num)
    
    return new_matrix

import numpy as np

if __name__ == '__main__':
    # mnr = input().rstrip().split()

    # m = int(mnr[0]) # Number of rows

    # n = int(mnr[1]) # Number of columns

    # r = int(mnr[2]) # Number of rotations
    

    # matrix = []

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    
    matrix = np.random.randint(10, size=(150,150)).tolist()
    
    final_result = targetRotation(150,150,matrix, 1)

    for each_result in final_result:
        # for each_element in each_result:
        print(len(each_result))
        print(*each_result)
    
    

    

    # matrix = [[1,2,3,4],[7,8,9,10],[13,14,15,16],[19,20,21,22],[25,26,27,28]]#547
    #matrix = np.random.randint(10, size=(150,150)).tolist()
    #matrix = [[1,1,1,1],[1,2,3,1],[1,4,5,1],[1,1,1,1]]
    # m = 5
    # n = 4
    # r = 1
    #new_final_result = targetRotation(m,n,matrix, r)
    
    # for each_result in new_final_result:
    #     print(*each_result)