order1={"tea","dosa","idily"}

order2={"coffee","dosa","puttu"}

orders=order1.intersection(order2)
print(orders)  # print common item from two set

common=order1.union(order2)
print(common) # print all elements and remove duplicates

diff=order1.difference(order2)
print(diff)  # print elemets whit 

print(order1.symmetric_difference(order2))

add=order1.add("freshlime")
print(order1) # add element in set

set_a={10,20,30}

set_b={100,10,200,20,300,30}

print(set_a.issubset(set_b)) # return true when all elements in set1 is included in set 2 else retrn  false.

print(set_b.issuperset(set_a))


print(set_a.symmetric_difference(set_b))  # remove common elements in two set and form new set.    #[a/b]u[b/a]

