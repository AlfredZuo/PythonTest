'''
    20. 有效的括号
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。
    示例 1：
    输入：s = "()"
    输出：true
    示例 2：
    输入：s = "()[]{}"
    输出：true
    示例 3：
    输入：s = "(]"
    输出：false
    提示：
    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成
'''
# s = "(]"
# s = "()[]{}"
# s = "(()[]{}"
# s = "{[]}"
# s = "]"
# s = "(){}}{"
# s = "(])"

class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # mark_hashtable = {'(': ')', '[': ']', '{': '}'}
        # for i, ch in enumerate(s):
        #     if ch in mark_hashtable:
        #         stack.append(ch)
        #     elif len(stack) == 0:
        #         print('1False')
        #         return False
        #     elif mark_hashtable.get(stack[-1]) == ch:
        #         stack.pop()
        #     else:
        #         print('3False')
        #         return False
        # if len(stack) == 0:
        #     print('True')
        #     return True
        # else:
        #     print('2False')
        #     return False

        """解法二，通过内置问号的方式规避越界问题"""
        mark_hashtable = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for i, ch in enumerate(s):
            if ch in mark_hashtable:
                stack.append(ch)
            elif mark_hashtable[stack.pop()] != ch:
                return False
        return len(stack) == 1
