"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = dict()
        for i, num in enumerate(nums):
            if num == hash_table.get(num):
                hash_table.pop(num)
                continue
            else:
                hash_table[num] = num
        # for k in hash_table.keys():
        #     print(k)
        #     return k
        l = list(hash_table.keys())
        print(l, hash_table.get(l[0]))
        return hash_table.get(l[0])
