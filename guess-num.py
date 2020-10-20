#產生一個隨機整數1~100 (不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1, 100)

count = 0	#計數用

while True:
	num = input('請猜數字： ')
	num = int(num)
	count += 1  # count = count + 1
	if num == r:
		print('你猜中了!!')
		break
	elif num > r:
		print('比答案大。')
	elif num < r:
		print('比答案小。')
	print('這是你猜的第', count, '次')
