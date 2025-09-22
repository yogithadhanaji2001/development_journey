# str -group of object
# immutable
num1=10

print(type(num1))

# name= "",'',""" """,str()

name = 'luminartec'

print(name.capitalize()) # first letter capital

print(name.casefold()) # lower case

print(name.index("tec")) # indicate the position  of str  moreover index not applicable with (int, float, bool)

print(name.isalpha()) # str object is alpha or not

num="123yog"
print(num.isdigit()) #str object is number or not

print(num.isalnum()) # str object contain both alph and number 



name="/nstrip/n"

trimed=name.strip("/n")

print(trimed) # remove the first and last specified character from str obj

print(name.rstrip("/n")) #remove the specific element from right side
print(name.lstrip("/n")) # remove the specific element form left side


name = "the quick brown fox jumb over lazy dog"

word= name.split(" ")

print(word)  # split the object

