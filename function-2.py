# encoding: utf-8

#範例一 3^2=9
def power(base, exp):
    print(base**exp)
power(3,2)

# 執行會印出：
# 3^2=9
#------------------------------------------------------------------
#範例二 4^0=1
def power(base, exp=1):
    print(base**exp)
power(4)  #雖然這邊只有給base值，沒有exp值，但第12行有說exp=1，所以還是可以執行的

# 執行會印出：
# 4^0=1
#------------------------------------------------------------------
#範例三 參數名稱對應 
def div(n1,n2):
    print(n1/n2)
power(2,4)  #雖然這邊只有給base值，沒有exp值，但第12行有說exp=1，所以還是可以執行的

# 執行會印出：
# 0.5因為n1=2 n2=4 n1/n2=0.5
#------------------------------------------------------------------
#範例四 參數名稱對應 
def div(n1,n2):
    print(n1/n2)
power(2,4)  #雖然這邊只有給base值，沒有exp值，但第12行有說exp=1，所以還是可以執行的
power(n2=2, n1=4)

# 執行會印出：
# 0.5因為n1=2 n2=4 n1/n2=0.5
# 2.0因為n1=4 n2=2 n1/n2=2.0    第31行雖然先寫n2 再寫n1但是還是可判讀
#------------------------------------------------------------------
#範例五 無限參數
def avg(*ns):
    print(ns)
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
# 執行會印出：
(3, 4)          
(3, 5, 10)
(1,4,-1,-8)
#------------------------------------------------------------------
#範例六 無限參數
def avg(*ns):
    for n in ns:
        print(n)
avg(3,4)
# 執行會印出：  把迴圈一個一個拿出來
# 3 
# 4 
#------------------------------------------------------------------ 
#範例七 無限參數   
def avg(*ns):       #不定長數參數處理，ns是tuple意思 用列表的長度
    sum =0
    for n in ns:
        sum = sum + n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
# 執行會印出：  把迴圈一個一個拿出來
# 3.5 = (3+4)/2 
# 6.0 = (3+5+10)/3
# -1.0= (1+4-1-8)/4
#------------------------------------------------------------------  
