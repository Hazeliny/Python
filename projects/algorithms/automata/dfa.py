'''
Requirement:
实现一个确定有限状态自动机(DFA),判断输入字符串是否被自动机接受。
transitions 是状态转移规则
start 是起始状态
final 是终止状态集合
string 是输入字符串
如果最终状态属于 final，返回 True，否则返回 False。
Concept:
有限状态自动机（FSA，或 FSM Finite State Machine）是一种数学模型，描述了一个系统在有限个状态之间的转换过程，通常用于模式匹配、词法分析、正则表达式处理等。它由以下五个部分组成：
有限个状态（States, S）
一个有限的状态集合 {q0, q1, q2, ...}。
输入字符集（Alphabet, Σ）
允许的输入符号，例如 {a, b}。
状态转换函数（Transitions, δ）
规定当前状态 遇到某个字符 后，应该跳转到哪个状态。
起始状态（Start state, s0）
程序一开始所处的状态，通常用 q0 表示。
终止状态集合（Final states, F）
如果输入字符串处理完后，自动机停留在 终止状态，则字符串被接受，否则不被接受。
'''

def DFA(transitions, start, final, string):

    cur = start
    # 逐步读取字符串中的字符并进行状态转移
    for char in string:
        if char not in transitions.get(cur,{}): # Avoid KeyError
            return False
        cur = transitions[cur][char]
    return cur in final  # 直接检查当前状态是否是终止状态

'''
    num = len(string)
    num_final = len(final)
    cur = start

    for i in range(num):
        if transitions[cur][string[i]] is None:
            return False
        else:
            cur = transitions[cur][string[i]]
    for i in range(num_final):
        if cur == final[i]:
            return True
    return False

'''
