hungry=True
if hungry:
    print("我就去吃飯")

rainy=False
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")
score=50
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")

score=90
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")

score=90
rainy=False
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")

score=90
rainy=True
if score!=100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(10,3,5))

