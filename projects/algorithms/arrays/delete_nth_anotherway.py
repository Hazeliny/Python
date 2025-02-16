'''
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
'''
import collections

# Time complexity O(n^2)
def delete_nth_naive(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n: # ❌ 这里每次都会扫描整个 ans 列表，所以性能更差
            ans.append(num)
    return ans

# Time Complexity O(n), using hash tables.
def delete_nth(array, n):
    result = []
    # 当defaultdict访问不存在的键时不会报KeyError，它会自动创建该键，并赋值为int()默认值，即0，自动初始化0
    counts = collections.defaultdict(int) # keep track of occurrences 用哈希表存储出现次数，O(1) 查询
    for i in array:
        if counts[i] < n: # ✅ O(1) 复杂度
            result.append(i)
            counts[i] += 1 # ✅ O(1) 复杂度
    return result

# test
lst = [1, 2, 3, 1, 2, 1, 2, 3]
N = 2
print(delete_nth(lst, N))
