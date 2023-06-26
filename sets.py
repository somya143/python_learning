s = {4,9,23,"somya"}  #in set we cannot print same element twice
info = {"carla",3,89,False,"somya",23}
som = {}
se = set()
print(s.union(info)) #this method merges two sets and doesn't repeat the same element
print(s.difference(info)) #this method prints only those elements from the first set which doesn't match with other set
print(s.intersection(info)) #this method only prints those elements which are common in both sets.
print(s.intersection_update(info))