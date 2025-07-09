#Append
list1= ["scotland","canada","kerala"]
print(list1)
list1.append("india")
print(list1)

#extend
#eg1
list2=[1,2,3,4,7]
list3=[15,29]
list2.extend(list3)
print(list2)
#eg2
list4=["kerala","telangana","kashmire"]
list5=["andhra","tamilnadu"]
list4.extend(list5)
print(list4)

#count
#eg1
fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'apple']
print(fruits.count('apple'))  # Output: 3
print(fruits.count('banana')) # Output: 1
print(fruits.count('mango'))  # Output: 0
#eg2
mylist=[22,23,15.29,28+13j,"hello"]
print(mylist.count(23))

#Mutability
mylist=["hello","ece",15,28.29,15+29j]
print(mylist)
mylist[3]="ramcharan"
print(mylist)

#insert
mylist=[22,23,35,67,89]
print(mylist)
mylist.insert(1,"hello")
print(mylist)

#index
mylist=[22,33,45,67,89,15,29] 
print(mylist.index(89))
print(mylist.index(29))

#remove
mylist=[1,2,3,5,6,7,8,9]
mylist.remove(5)
print(mylist)

#pop
mylist=[34,15.29,28+13j,"hello",19]
print(mylist)
mylist.pop(4)
print(mylist)

#reverse
mylist=[15.29,28,13,21+5j,"teju"]
mylist.reverse()
print(mylist)

#copy
mylist=[22,33,44,55,66,77,88]
print(mylist)
mylist2=mylist.copy()
print(mylist2)

#clear
mylist=[22,33,77]
print(mylist.clear())
print(mylist)

#sort
mylist=[23,45,67,89,90]
mylist.sort()
print(mylist)
