#Zip function aggregates elements from 2 or more iterables and creates a zip object in the form
#of tuples
#Syntax zip(*iterables)

name=["Ammar","Hassan","Haroon","Sameer"]
phone_num=[92309,92301,92302,92308]
combination=list(zip(name,phone_num))
print(combination)