#for 變數 in 字串OR列表:
#     要重複的程式碼
for letter in "小白你好":
    print(letter)

for num in [0,1,2,3,4]:
    print(num)
#range(100)=[0,1,2,...,99]

for num in range(100):
    print(num)

for num in range(2,7):
    print(num)


#print(pow(2,5))
#2*2*2*2*2

def power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result*=base_num
    return result

print(power(2,5))
