# 猜數字 random
import random
start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結整值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0  # 變數寫在while的外面，在重複迴圈時才不會一直歸零
while True:
    count = count + 1  # 也可以寫成 count += 1
    num = input('請猜數字(1~100)： ')
    num = int(num)
    if num == r:
        print('你猜中了!!')
        print('你一共猜了', count, '次') # 因遇到break就會跳出迴圈，在這也印出最終的次數
        break
    elif num > r:
        print('比答案大。')
    elif num < r:
        print('比答案小。')
    print('這是你猜的第', count, '次')  # 寫在if的架構外，就不用重複寫