# class dict:
#     def get(key):
#     def pop(key): # remove the key value
#     def keys():  # return all keys 
#     def values() # return all values
#     def items()
#     def update ()



fruits={"a":"apple","b":"banana","c":"cherry","d":"dragon-fruit"}

print(fruits["a"])

# to take value use get method becasue in [] if the keyy  is not avaliable there the error occured in case of get it will return none.

print(fruits.get("b"))

fruits.pop("d")
print(fruits)

print(fruits.keys())

# itreating all keys

# for k in fruits.keys():
#     print(k)


for v in fruits.values():
    print(v)


for k,v in fruits.items():

    print(k,v)



fruits.update(o="orange")
fruits.update(e="egg fruit")

print(fruits)

# mutable 
# duplicates are not allowed

