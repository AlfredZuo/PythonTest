"""
217. 存在重复元素
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
示例 1：
输入：nums = [1,2,3,1]
输出：true
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = dict()
        for i, num in enumerate(nums):
            if num == hash_table.get(num):
                print(hash_table, True)
                return True
            else:
                hash_table[num] = num
        print(hash_table, False)
        return False
