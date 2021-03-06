# _*_coding:utf-8_*_
# 题目：假设有n个活动，这些活动要占用同一片场地，而场地在某时刻只能供一个活动使用。
# 注意：每个活动都有一个开始时间和结束时间（题目中为了方便，使用整数表示） 区间表示活动在（1,2）内占用场地，区间为左开右闭
# 问题：安排哪些活动能够使该场地举办的活动的个数最多？

'''
解析：这里使用贪心算法求解，其中贪心的结论就是：最先结束的活动一定是最优解的一部分
（这个在数学上可以证明）
证明的题目是：假设a是所有的活动中最先结束的活动，b是最优解中最先结束的活动，那么a一定是b的一部分（即最先结束的活动一定是最优解的一部分）
如果说 a==b，那么结论成立
如果说 a!=b，则b的结束时间一定晚于a的结束时间
  所以此时用a替换掉最优解中的b，a一定不与最优解中的其他活动时间重叠，因此替换后的解也是最优解
  所以我们的问题得解。
'''

# 一个元组表示一个活动，（开始时间，结束时间， 注意：左开右闭）
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11),
              (8, 12), (2, 14), (12, 16)]

# 保证活动是按照结束时间排好序,我们可以自己先排序
activities.sort(key=lambda x:x[1])

def activity_selection(a):
    # 首先a[0] 肯定是最早结束的
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 当前活动的开始时间小于等于最后一个入选活动的结束时间
            # 不冲突
            res.append(a[i])
    return res

res = activity_selection(activities)
print(res)
# [(1, 4), (5, 7), (8, 11), (12, 16)]

