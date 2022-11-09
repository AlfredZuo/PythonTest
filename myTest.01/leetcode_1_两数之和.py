# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         length = len(nums)
#         result = []
#         for i in range(length):
#             for j in range(1, length - i):
#                 if nums[i] + nums[i + j] == target:
#                     result.append(i)
#                     result.append(i + j)
#                     print(result)
#                     return result

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        records = dict()
        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]  # 如果存在就返回字典记录索引和当前索引


    '''
    很明显暴力的解法是两层for循环查找，时间复杂度是O(n^2)。
    本题呢，则要使用map，那么来看一下使用数组和set来做哈希法的局限。
    数组的大小是受限制的，而且如果元素很少，而哈希值太大会造成内存空间的浪费。
    set是一个集合，里面放的元素只能是一个key，而两数之和这道题目，不仅要判断y是否存在而且还要记录y的下表位置，因为要返回x 和 y的下表。所以set 也不能用。
    此时就要选择另一种数据结构：map ，map是一种key value的存储结构，可以用key保存数值，用value在保存数值所在的下表。
    C++中map，有三种类型： 如图
    std::unordered_map 底层实现为哈希表，std::map 和std::multimap 的底层实现是红黑树。
    同理，std::map 和std::multimap 的key也是有序的（这个问题也经常作为面试题，考察对语言容器底层的理解）。 更多哈希表的理论知识请看关于哈希表，你该了解这些！。
    这道题目中并不需要key有序，选择std::unordered_map 效率更高！使用其他语言的录友注意了解一下自己所用语言的map结构的内容实现原理。
    接下来需要明确两点：
    map用来做什么
    map中key和value分别表示什么
    map目的用来存放我们访问过的元素，因为遍历数组的时候，需要记录我们之前遍历过哪些元素和对应的下表，这样才能找到与当前元素相匹配的（也就是相加等于target）
    接下来是map中key和value分别表示什么。
    这道题 我们需要 给出一个元素，判断这个元素是否出现过，如果出现过，返回这个元素的下标。
    那么判断元素是否出现，这个元素就要作为key，所以数组中的元素作为key，有key对应的就是value，value用来存下标。
    所以 map中的存储结构为 {key：数据元素，value：数组元素对应的下表}。
    在遍历数组的时候，只需要向map去查询是否有和目前遍历元素比配的数值，如果有，就找到的匹配对，如果没有，就把目前遍历的元素放进map中，因为map存放的就是我们访问过的元素。
    '''