# _*_ coding: utf-8 _*_
# @Time     : 2022/6/15 11:29
# @Author   : Mr_Li
# @FileName : guess the number.py
# 首先导入Python随机模块
import random

# 设置随机数
x = random.randint(0, 9)
# 设置循环起点
i = 1
# 定义循环
while i < 4:
    # 打印分割线
    print(100 * '-')
    input_number = input('输入一个0-9的数字：')
    if not input_number.isdigit():
        print("请输入一个数字,输入的不是数字将重新开始")
        continue
    elif int(input_number) < 0 or int(input_number) > 9:
        print('输入的数字大小不符合规范，应在0-9之间，请重新输入')
        continue
    else:
        f = 3 - i
        if int(input_number) < x:
            print('小了，猜大一点的数，你猜的数是：%s,你还有%s次机会' % (input_number, f))
        elif int(input_number) == x:
            print('恭喜你猜对了!随机生成的数是：%s' % x)
            break
        elif int(input_number) > x:
            print('大了，猜小一点的数，你猜的数是：%s,你还有%s次机会' % (input_number, f))
    i = i + 1
    if i == 4:
        print("你真笨，猜%s次都不正确,还请下次努力!本次的随机数是：%s" % (i-1, x))