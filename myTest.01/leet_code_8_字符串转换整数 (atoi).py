"""
    8. 字符串转换整数 (atoi)
    请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
    函数 myAtoi(string s) 的算法如下：
    读入字符串并丢弃无用的前导空格
    检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
    返回整数作为最终结果。
    注意：
    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
    0 <= s.length <= 200
    s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
"""
# 圈复杂度会很高，需要优化
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s_lst = []
#         manipulated_list = []
#         number_flag = False
#         for i, ch in enumerate(s):
#             if ch != ' ':
#                 s_lst.append(ch)
#                 if '0' <= ch <= '9' or ch == '+' or ch == '-':
#                     number_flag = True
#             elif ch == ' ' and number_flag:
#                 break
#         if len(s_lst) == 0:
#             return 0
#         if s_lst[0] == '-':
#             minus_flag = True
#             mark_flag = True
#         elif s_lst[0] == '+':
#             minus_flag = False
#             mark_flag = True
#         else:
#             minus_flag = False
#             mark_flag = False
#         print(s_lst, mark_flag, minus_flag)
#         if mark_flag:
#             s_lst.pop(0)
#         print(s_lst, mark_flag, minus_flag)
#         for i, ch in enumerate(s_lst):
#             if '0' <= ch <= '9':
#                 manipulated_list.append(ch)
#                 continue
#             else:
#                 break
#         print(manipulated_list, s_lst, mark_flag, minus_flag)
#         if len(manipulated_list) > 0:
#             result = int(''.join(manipulated_list))
#         else:
#             result = 0
#         if minus_flag:
#             result = 0 - result
#         if result < - 2 ** 31:
#             result = - 2 ** 31
#         if result > 2 ** 31 - 1:
#             result = 2 ** 31 - 1
#         print(result, manipulated_list, s_lst, mark_flag, minus_flag)
#         return result

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1  # 1表示正号，-1表示负号
        self.answer = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_current_char_type(self, input_char: str) -> int:
        if input_char.isspace():
            return 0
        elif input_char == '-' or input_char == '+':
            return 1
        elif input_char.isdigit():
            return 2
        else:
            return 3

    def get(self, input_char: str):
        self.state = self.table[self.state][self.get_current_char_type(input_char)]
        if self.state == 'in_number':
            self.answer = self.answer * 10 + int(input_char)
            self.answer = min(self.answer, INT_MAX) if self.sign == 1 else min(self.answer, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if input_char == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        am = Automaton()
        for i, ch in enumerate(s):
            am.get(ch)
        print(am.answer * am.sign)
        return am.answer * am.sign
