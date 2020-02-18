currenInfoCount = 12
currenInfoCount = str(currenInfoCount)
if len(currenInfoCount) < 10:
    currenInfoCount = (10 - len(currenInfoCount)) * "0" + str(currenInfoCount)
    print(currenInfoCount)

elif len(currenInfoCount) == 10:
    currenInfoCount = str(currenInfoCount)
    print(currenInfoCount)

currenInfoCount =int(currenInfoCount)
print(currenInfoCount)

