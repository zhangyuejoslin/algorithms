import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

def dict_insertion(range_num):
    test_dict = {}
    for _ in range(range_num):
        each_n = random.randint(0, 20)
        test_dict[each_n] = each_n



def add_root(e,key):
    ''''
     e is node's name
    key is the node's key search
    '''
    bst=dict()
    bst[e]={'key':key,'P':None,'L':None,'R':None}
    return bst
def root(tree):
   for k,v in tree.items():
       if v['P'] == None:
           return k

def insert(tree, node, key):
    tree[node]={'key':key,'P':None,'L':None,'R':None}
    y =None
    x = root(tree)
    node_key = tree[node]['key']
    while x is not None:
        y=x
        node_root=tree['R']['key']
        if node_key < node_root:
            x=tree[x]['L']
        else:
            x=tree[x]['R']
    tree[node]['P']=y
    if y is not None and node_key< tree[y]['key']:
        tree[y]['L']=node
    else:
        tree[y]['R']=node

    return  tree


def print_all(tree):
   for k,v in tree.items():
       print(k,v)
       print()
'''
Give a root node and key search target 
Returns the name of the node with associated key 
Else None
'''
def tree_search(tree,root, target):
    if root ==None:
        print(" key with node associate not found")
        return root
    if tree[root]['key'] == target:
        return  root
    if target < tree[root]['key']:
        return tree_search(tree,tree[root]['L'],target)
    else:
        return  tree_search(tree,tree[root]['R'],target)

def tree_iterative_search(tree,root,target):
    while root is not  None and tree[root]['key']!=target:
        if target < tree[root]['key']:
            root=tree[root]['L']
        else:
            root=tree[root]['R']

    return root

def minimum(tree,root):
    while tree[root]['L'] is not None:
        root=tree[root]['L']
    return tree[root]['key']


def insert_binary_tree(range_num):
    bst=add_root('R',20)
    for _ in range(range_num):
        each_n = random.randint(0, 20)
        bst=insert(bst,str(each_n),each_n)


dict_insert_start_time = 0
dict_insert_end_time = 0 

dict_binary_start_time = 0
dict_binary_end_time = 0

count = 0
n = 2000
dict_insert_list = []
dict_binary_list = []
while count<30:
    each_dict_insert_list = []
    each_dict_binary_list = []
    for each_i in range(0,n):
        dict_insert_start_time = time.time()
        dict_insertion(each_i)
        dict_insert_end_time = time.time()
        each_dict_insert_list.append(dict_insert_end_time-dict_insert_start_time)

        dict_binary_start_time = time.time()
        insert_binary_tree(each_i)
        dict_binary_end_time = time.time()
        each_dict_binary_list.append(dict_binary_end_time-dict_binary_start_time)

    dict_insert_list.append(each_dict_insert_list)
    dict_binary_list.append(each_dict_binary_list)
    count += 1

dict_insert_list = np.mean(np.array(dict_insert_list),axis=0)
dict_binary_list = np.mean(np.array(dict_binary_list),axis=0)

y_insert = [y1 for y1 in dict_insert_list]
y_binary = [y2 for y2 in dict_binary_list]
x_list = [x for x in range(2000)]

x_major_locator=MultipleLocator(200)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x_list, y_insert, color='r', linewidth=1, alpha=0.6, label="insert")
ax.plot(x_list, y_binary, color='b', linewidth=1, alpha=0.6, label="binary")

plt.savefig('/VL/space/zhan1624/CV_homework/algorithm_homework/output_image/dict_comparison_10.png')
