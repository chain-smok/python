# open("檔案路徑",mode="開啟模式")
file=open("123.txt",mode="r")
print(file.readline())
print(file.readline())
for line in file:
   print(line)
print(file.readlines())
file.close()