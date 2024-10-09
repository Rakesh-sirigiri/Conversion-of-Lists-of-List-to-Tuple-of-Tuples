list = [['Rakesh', 'is', 'Best'], ['Rakesh', 'is', 'love'], ['Rakesh', 'is', 'for', 'Raviteja']]
print("The original list is : " + str(list))
res = tuple(tuple(sub) for sub in list)
print("The converted data : " + str(res))
