'''
    38. 外观数列
    给定一个正整数 n ，输出外观数列的第 n 项。
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
    你可以将其视作是由递归公式定义的数字字符串序列：
    countAndSay(1) = "1"
    countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
    前五项如下：
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    6.     312211
    7.     13112221
    8.     1113213211
    9.     31131211131221
    第一项是数字 1
    描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
    描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
    描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
    描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
    要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。
    然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。
    要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
    1. Create a helper function that maps an integer to pairs of its digits and their frequencies.
    For example, if you call this function with "223314444411",
    then it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].
    2. Create another helper function that takes the array of pairs and creates a new integer.
    For example, if you call this function with [[2,2], [3,2], [1,1], [4,5], [1, 2]],
    it should create "22"+"23"+"11"+"54"+"21" = "2223115421".
    3. Now, with the two helper functions, you can start with "1" and call the two
    functions alternatively n-1 times. The answer is the last integer you will obtain.
'''


# 以下是按照解题思路输出的
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             print('input 1, return 1')
#             return '1'
#         result = 1
#         for i in range(n - 1):
#             n_list = self.map_int_to_pair_with_description(result)
#             result = self.map_pair_with_description_to_int(n_list)
#         print(result)
#         return str(result)
#
#     def map_int_to_pair_with_description(self, n: int) -> list():
#         n_list = list(str(n))
#         result = list()
#         print(n_list)
#         n_list_length = len(n_list)
#         i = 0
#         while i < n_list_length:
#             count = 0
#             for j in range(n_list_length - i):
#                 if n_list[i] == n_list[i + j]:
#                     count += 1
#                 else:
#                     break
#             result.append([int(n_list[i]), count])
#             i += count
#         print(result)
#         return result
#
#     def map_pair_with_description_to_int(self, lst: list()) -> int:
#         int_lst = []
#         for i, pair in enumerate(lst):
#             int_lst.append(str(pair[1]))
#             int_lst.append(str(pair[0]))
#         int_str = ''.join(int_lst)
#         result = int(int_str)
#         print(result)
#         return result

#解法二，官方解法，但是官方描述读不懂
class Solution:
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'

        # 从第 2 项开始
        for _ in range(1, n):
            # 这里注意要将 cur 赋值给 pre
            # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            pre = cur
            # 这里 cur 初始化为空，重新拼接
            cur = ''
            # 定义双指针 start，end
            start = 0
            end = 0
            # 开始遍历前一项，开始描述
            while end < len(pre):
                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # 元素出现次数与元素进行拼接
                cur += str(end - start) + pre[start]
                # 这里更新 start，开始记录下一个元素
                start = end

        return cur

