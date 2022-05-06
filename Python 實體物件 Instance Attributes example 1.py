# encoding: utf-8

#範例一
# Point 實體物件的設計：平面座標上的點
class Point:
    #定義初始化函式
    def __init__(self):
        #根據要定義的東西，本例子為平面座標的點
        self.x=3
        self.y=4
#定義這個類別是為了建立第一個實體物件
p1=Point()
print(p1.x, p1.y) #透過實體物件包裝資料，實體物件.屬性名稱 抓到(3, 4)，建立並且使用

# 執行會印出：
# (3, 4)
#------------------------------------------------------------------
#範例二
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self):
        self.x=3
        self.y=4
#建立第一個實體物件
p1=Point()
print(p1.x, p1.y)

#建立第二個實體物件
p2=Point()
print(p2.x, p2.y)

# 執行會印出：
# (3, 4) 印出第一份資料 3,4
# (3, 4) 印出第二份資料 3,4
#------------------------------------------------------------------
# 範例三
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y): 
        self.x=3
        self.y=4
#建立第一個實體物件
p1=Point()
print(p1.x, p1.y)

#建立第二個實體物件
p2=Point()
print(p2.x, p2.y)

# 執行會印出：
# (3, 4) 印出第一份資料 3,4
# (3, 4) 印出第二份資料 3,4
#------------------------------------------------------------------
#範例四
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y):   #透過參數做變化
        self.x=x
        self.y=y
#建立第一個實體物件
p1=Point(3,4)           #建立一個實體物件 3放到x 4放到y
print(p1.x, p1.y)

#建立第二個實體物件
p2=Point(5,6)           #建立一個實體物件 5放到x 6放到y
print(p2.x, p2.y)

# 執行會印出：
# (3, 4) 印出第一個點 3,4
# (5, 6) 印出第二個點 5,6
#------------------------------------------------------------------
#範例五 FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName:
    #定義一個初始化的函式
    def __init__(self):
        self.first="Chou"   #建立 名
        self.last="Yin"     #建立 姓
#建立一個實體物件
name1=FullName()
print(name1.first, name1.last)

# 執行會印出：
# ('Chou', 'Yin')
#------------------------------------------------------------------
#範例六 FullName 實體物件的設計：分開紀錄姓、名資料的全名 建立彈性
#定義類別，是為了產生實體物件
class FullName:
    def __init__(self, first, last): #要彈性，透過初始化函式的參數
        self.first=first
        self.last=last

#實體物件第一組   第一個名字
name1=FullName("Chou", "Yin")   
#操作實體物件的屬性
print(name1.first, name1.last) 

#實體物件第二組   第二個名字
name2=FullName("Kobe", "Bryant")
#操作實體物件的屬性
print(name2.first, name2.last)

# 執行會印出：
# ('Chou', 'Yin')
# ('Kobe', 'Bryant')
#------------------------------------------------------------------
