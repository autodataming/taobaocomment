# -*- coding:utf-8-*-
import datetime

'''

时间过期函数
输入: 
	year 年
	month 月
	day 日
输出:
	第一个返回参数:True 表示时间过期,False 表示时间没过期
	第二个返回参数:表示剩余过期天数

example:

	if __name__ == '__main__':
		# 明天的时间
		year = 2016
		month = 7
		day =19
		ispass,remainday = ispasstime(year,month,day)
		if ispass:
			print("还没有过期,剩余天数:"+str(remainday))
		else:
			print("已经过期,过期天数"+str(remainday))

'''
def ispasstime(year,month,day):
	# 今天的时间
	nowtoday = datetime.datetime.today()
	# 过期时间
	passday = datetime.datetime(year,month,day)
	# 剩余天数
	remaindays = (nowtoday-passday).days
	# 判断
	if remaindays <= 0:
		return True,-remaindays
	else:
		return False,remaindays


if __name__ == '__main__':
	# 明天的时间
	year = 2016
	month = 7
	day =18
	ispass,remainday = ispasstime(year,month,day)
	if ispass:
		print("还没有过期,剩余天数:"+str(remainday))
	else:
		print("已经过期,过期天数"+str(remainday))