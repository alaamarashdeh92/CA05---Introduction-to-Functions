# Q 7
# ******

def sum_or_max(my_list):
    if len(my_list) %2 == 0 :
        return sum(my_list)
    if len(my_list) != 0 :
        return max(my_list)
list1 = [1,2,3,4,5]  
print(sum_or_max(list1))

