#.sort() is used for sorting mutable items and sorted() is used for sorting immutable
#items

#-------------------------------------------List------------------------------
names=["Ammar","Ali","Ahmad","Undertaker","John Cena"]
names.sort()
print(names)

#------------------------Tuples------------------------

grades=(13,214,123,123,13,32,2312,32,231,123,32)
grades=sorted(grades)
print(grades)

#------------------------Dictionary------------------------

grades={"Ammar":3.61,"Awaim":3.84,"Fateh":3.79,"Saad":3.77}
sorted_by_names=dict(sorted(grades.items()))
print(sorted_by_names)

reverse_sorted_by_names=dict(sorted(grades.items(),reverse=True))
print(reverse_sorted_by_names)

sorted_by_keys=sorted(grades.items(),key=lambda x:x[1])
print(sorted_by_keys)

sorted_by_keys_reverse=sorted(grades.items(),key=lambda x:x[1],reverse=True)
print(sorted_by_keys_reverse)