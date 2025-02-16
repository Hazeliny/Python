'''
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
'''
# 注：如num在字典中不存在时count_dict[num]不会自动初始化为0，所以不能写作count_dict[num] += 1，会报错KeyError
def limit_occurrences(lst, N):
    result = []
    count_dict = {}

    for num in lst:
        if count_dict.get(num, 0) < N: # count the occurrences of num in result如果 num存在于 count_dict，则返回 num对应的值（即num目前的计数），否则返回0
            result.append(num)
            count_dict[num] = count_dict.get(num, 0) + 1 # update the occurrences这样写可以安全初始化并递增，不会报错KeyError
    return result

# test
lst = [1, 2, 3, 1, 2, 1, 2, 3]
N = 2
print(limit_occurrences(lst, N))
