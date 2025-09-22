
# set is created as 

set={10,20,12,True,"hari",10}

# or

# set=set()

print(type(set))

print(set)

# unoderes | indexing not supporting
# duplicates are not allowed
# mutable


st1={10,20,30,40}
st2={100,10,200,20,300}


# common element

intersection=st1.intersection(st2)

print(intersection)


union_set=st1.union(st2)

print(union_set)

diff=st1.difference(st2)
print(diff)

