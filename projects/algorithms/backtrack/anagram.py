"""
相同字母异序词
Given two strings, determine if they are equal after reordering.

Examples:
"apple", "pleap"  -> True
"apple", "cherry" -> False
"""

def anagram(s1, s2):
    c1 = [0] * 26 #创建一个长度为26的一维列表，所有元素初始化为0
    c2 = [0] * 26

    for c in s1:
        pos = ord(c) - ord('a')
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c) - ord('a')
        c2[pos] = c2[pos] + 1
    
    return c1 == c2

#创建二维列表：c2 = [[0] * 26 for _ in range(26)]
#创建二维列表不能写成[[0] * 26] * 26， 它会导致所有行共用同一个列表对象，修改一行会影响所有行
