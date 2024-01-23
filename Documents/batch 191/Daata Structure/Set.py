#4.Set{}:   #to not allow duplicate

set1={1,2,3,4,5,6}
set2={5,6,7,8,9,10}
print(set1 & set2)   #'&' for set intersection
print(set1 | set2)   #'|' for set union
print(set1 - set2)   #set difference
print(set1 ^ set2)   #set symmatic difference - don't print common data

set1.add(100)   #add values
print(set1)

