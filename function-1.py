#encoding: utf-8

#範例一
def greet():
    print("可以不用重複打第一行")
    print("可以不用重複打第二行")
greet()

# 執行會印出：
# 可以不用重複打第一行
# 可以不用重複打第二行

#範例二
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("function 成功")

greet("Chou Po", "Yin")

# 執行會印出： 照理來說會印出，但是出現SyntaxError: invalid syntax
# Hi Chou Po Yin
# function 成功

#範例三
def multiply():
    print(3*4)

#呼叫函式
multiply()   

# 執行會印出：
# 12


#範例四
def multiply(n1, n2):
    print(n1*n2)

#呼叫函式
multiply(3,4)   #會印出3*4 可隨意執行 n1*n2
multiply(1,2)   #會印出1*2 可隨意執行 n1*n2

# 執行會印出：
# 12
# 2

#範例五
def multiply(n1, n2):
    print(n1*n2)

value=multiply(3,4)     
print(value)            

# 執行會印出：
# 12   #回傳12
# None #結束函式 回傳None
