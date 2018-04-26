#coding: utf-8


'''
小明在过年期间胖了很多，打算通过爬楼梯来减肥。他看到健身指南上说，一次爬一个台阶大概会燃烧N1克脂肪，爬2个台阶会燃烧N2克脂肪，爬3个台阶会燃烧N3克脂肪。可是小明的体力非常弱，只够爬一次M个台阶，并且连续爬2次三个台阶，连续爬4次两个台阶之后，都必须走3步台阶休息下(注这三步台阶不消耗能量)，所以他想设计一下策略，让每次爬完楼梯能够燃烧最多的脂肪。

编译器版本: Python 2.7.6
请使用标准输出(sys.stdout)；已禁用图形、文件、网络、系统相关的操作，如Process , httplib , os；缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用；如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(' ')进行截取；建议使用raw_input()
时间限制: 1S (C/C++以外的语言为: 3 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
第一行，整数N1，N2，N3，M（分别表示一个台阶消耗脂肪量，二个台阶消耗脂肪量，三个台阶消耗脂肪量，台阶总数：1<N1,N2,N3<=100，10<M<200）。
输出:
输出爬完台阶能够燃烧的脂肪总克数。
输入范例:
1,3,5,15
输出范例:
24

#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
/** 请完成下面这个函数，实现题目要求的功能 **/
 /** 当然，你也可以不按照这个模板来作答，完全按照自己的想法来 ^-^  **/

def  Arrange(n):

try:
    _n = raw_input()
except:
    _n = None

  
res = Arrange(_n)

print str(res) + "\n"

'''

import sys
import os
import re
#** 请完成下面这个函数，实现题目要求的功能 **/
# /** 当然，你也可以不按照这个模板来作答，完全按照自己的想法来 ^-^  **/
# 贪心算法即可 
def  Arrange(n):
	n1,n2,n3 = 0,0,0
	_list = []
	_list = n.split(',')
	_list = map(int,_list)
	print _list
	cost0 = []
	M = int(_list[3])
	#计算各个方式每台阶的消耗量和走的台阶数  [[平均每台阶消耗卡路里, 台阶数, 总消耗卡路里],......]
	cost0.append([_list[0] /1.0, 1, _list[0]])
	cost0.append([_list[1] /2.0, 2, _list[1]])
	cost0.append([_list[1] * 4 / (2*4.0+3.0), 11, _list[1]*4])
	cost0.append([_list[2] /3.0, 3, _list[2]])
	cost0.append([_list[2] * 2 / (3*2.0+3.0), 9, _list[2]*2])

	temp_num = 0
	# 按消耗量降序排列原来的情况,即穷尽情况
	Cost_sorted = sorted(cost0, key = lambda cost: cost[0], reverse = True)
	print Cost_sorted
	output = 0.0
	step = [] #记录一次走几个台阶
	while M > 0:
		# next_step = False
		for i in range(len(Cost_sorted)):
			if (step) and (Cost_sorted[i][1] == step[-1])  and (step[-1] == 2 or step[-1] == 3): #判断这一步是不是 2步台阶或者3步
			# if (len(step) >0) and (Cost_sorted[i][1] == step[-1])  and (step[-1] == 2 or step[-1] == 3)
				continue
			elif M >= Cost_sorted[i][1]:
				M = M - Cost_sorted[i][1] 
				step.append(Cost_sorted[i][1])
				output += Cost_sorted[i][2]

				break
				# next_step = True
			else:
				continue
	return int(output)
try:
    _n = raw_input()
except:
    _n = None
  
res = Arrange(_n)
print str(res) + "\n"
