#filter function returns all elements of a collection that a pass a condition
#Syntax->filter(function,collection)

age=[19,18,23,13,9,90,23,12,32,2,3]
adult=filter(lambda a:a>=18,age)
for i in adult:
    print(i)