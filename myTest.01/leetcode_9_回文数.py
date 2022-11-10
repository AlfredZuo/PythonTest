"""
9. 回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = []
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            while x != 0:
                x_list.append(x % 10)
                x //= 10
            x_length = len(x_list)
            print(x_list, x_length)
            if x_length % 2 == 1:  # 长度是奇数
                for i in range(x_length // 2 + 1):
                    if x_list[x_length // 2 - i] == x_list[x_length // 2 + i]:
                        continue
                    else:
                        print(False)
                        return False
            else:  # 长度是偶数
                for i in range(x_length // 2):
                    if x_list[x_length // 2 - 1 - i] == x_list[x_length // 2 + i]:
                        continue
                    else:
                        print(False)
                        return False
            print(True)
            return True
