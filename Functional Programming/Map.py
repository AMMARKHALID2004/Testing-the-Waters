#Map function is used to apply a function to all items in a collection
#Syntax->map(function,collection)
celsius=[0,12,42,24,21,45,53]

fahrenheit=map(lambda temp:((temp*1.8)+32),celsius)
for each in fahrenheit:
    print(each)

mass=[123,45,47,132,67,243,65,312]
acc=[12,34,321,21,2,12,31,12]
force=list(map(lambda m,a:m*a,mass,acc))
print(force)
