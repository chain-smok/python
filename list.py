scores=[90,70,60,50,80]
friends=["小黑","小黃","小綠"]
things=[90,"小黑",True]
print(scores[-2])
print(scores[1:4])
print(scores[1:])
print(scores[:4])
scores[0]=30
#scores.extend(friends)
scores.append(30)
scores.insert(2,40)
scores.remove(30)
scores.pop()
scores.sort()
scores.reverse()
print(scores.count(70))
print(scores)
scores.clear()
print(scores)