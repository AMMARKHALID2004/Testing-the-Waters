#Reduce function reduces the items in a collection to a single value
#Syntax->reduce(function,collection)
#Note:for loop is a typical approach rather than reduce
from functools import reduce

num=[234,35,42,35,4,2,532,42,523,2,532,2,53.2,4.0,244,213]

add=reduce(lambda x,y:x+y,num)
print(add)