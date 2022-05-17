# _*_ coding: utf-8 _*_
# @Time     : 2022/4/26 17:04
# @Author   : Mr_Li
# @FileName : cs_test.py


# def mx_tt(p):
#     n = len(p)
#     for a in range(n):
#         for b in range(0, n - a - 1):
#             if p[b] > p[b + 1]:
#                 p[b], p[b + 1] = p[b + 1], p[b]
#
#
# p = [2, 2, 45, 1, 12, 46, 78, 56, 44, 98, 66]
# mx_tt(p)
# print('排序结果：')
# for a in range(len(p)):
#     print('%d' % p[a])


# print('两数之和为 %.0f' % (float(input('输入第一个数字：')) + float(input('输入第二个数字：'))))
# print(random.randint(float(input('输入第一个数字：')), float(input('输入第二个数字：'))))
import random
a = random.randint(0, 9)
b = random.randint(10, 99)
print(a)
print(b)
print(a + b)
print(random.randint(a, b))

