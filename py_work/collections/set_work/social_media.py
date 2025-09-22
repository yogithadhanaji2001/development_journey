

sachin_friends=["yogi","dhanu","rupa","kolli","raina","dhoni","lakshmi","gauri"]
sachu_friends=["yogi","dhanu","rupa","kolli","raina","sachin","ashi"]

# display all user

sachin_friends=set(sachin_friends)
sachu_friends=set(sachu_friends)

print(sachin_friends.union(sachu_friends))


# display unique friens of sachin

print(sachin_friends.difference(sachu_friends))

# mutal friends

mutal_friends=sachin_friends.intersection(sachu_friends)

print(len(mutal_friends))


