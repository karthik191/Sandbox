import itertools
from datetime import datetime
list1 = list(range(0,100))
list2 = list(range(0,150))
list3 = list(range(0,300))

startTimeItertools = datetime.now()
count = 0
for x,y,z in itertools.product(list1,list2,list3):
    count +=1
    print(x,y,z)
runTimeForIterTools = datetime.now() - startTimeItertools

startTimeForLoop = datetime.now()
for x in list1:
    for y in list2:
        for z in list3:
            print(x,y,z)
runTimeNestedForLoop = datetime.now() - startTimeForLoop

print(runTimeForIterTools,runTimeNestedForLoop)

