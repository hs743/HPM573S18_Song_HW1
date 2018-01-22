yours = ['Yale','MIT','Berkeley']
Mine = ['Harvard','Columbia','Cornell']
ours1 = Mine + yours
print(ours1)
ours2 = []
ours2.append(Mine)
ours2.append(yours)
print(ours2)
yours[1] = 'Stanford'
print(yours)
print(ours1)
print(ours2)
#The difference between ours1 and ours2 is element of ours2 is list, put it another way, the number of dimention between
#ours2 and ours1 is different.
#The reason is the difference between deepcopy and shallowcopy. For ours2, it is deepcopy.