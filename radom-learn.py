import random
#從列表隨機取一個資料
data=random.choice([1,4,6,9])
print(data)
#從列表中隨機取n個資料，n < 列表數量
data=random.sample([1,2,3,4,5,6], 5)
print(data)
#隨機調換資料（修改原列表） ，就地修改data列表
data=[1,2,3,4]
random.shuffle(data)
print(data)
#取0~1中的隨機數字，每個數字出現機率『相同』，random.random()=random.uniform(0.0,1.0)
print(random.random())
print(random.uniform(0.0, 1.0))
 #指定範圍，uniform指機率相同
print(random.uniform(60, 100))

#常態分配
#取平均數100，標準差10
#常態分配亂數
print(random.normalvariate(100,10))