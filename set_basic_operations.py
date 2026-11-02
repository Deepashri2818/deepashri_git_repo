a = {11,11,12,5,1,0,True,False,"Deeps"}
#set will remove duplicate value 
# True =1, False=0 since it has values 1 and 0 in set it wont print again
print()
print(a)
a.add(55)
print(a)

print()
a.remove(11)
print(a)

print()
a.discard(1)  #this is main method to remove  value frm set
print(a)

print()
a.clear()
print(a)