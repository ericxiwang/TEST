import random 
import bisect

weight = {'AL':0.1,'AU':0.1,'AT':0.1,'BE':0.1,'BR':0.2,'CA':0.4,'CL':0.1,'CN':0.3,'CO':0.1,'EG':0.1,'FR':0.1,'DE':0.1,'GR':0.1,'HK':0.1,'IN':0.2,'ID':0.1,'IL':0.1,'IT':0.1,'JP':0.2,'KP':0.1,'MX':0.1,'ES':0.1,'SG':0.1,'TR':0.1,'GB':0.1,'US':0.3}
#weight = {'a':0.3,'b':3.2,'c':2.4}
items = weight.keys()
print items
mysum = 0
breakpoints = [] 
for i in items:
    mysum += weight[i]
    breakpoints.append(mysum)

def getitem(breakpoints,items):
    score = random.random() * breakpoints[-1]
    i = bisect.bisect(breakpoints, score)
    return items[i] 

print getitem(breakpoints,items)