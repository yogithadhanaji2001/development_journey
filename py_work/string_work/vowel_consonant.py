# read a text from user and desplay vowel count and consonent count

text= "hello world wellcome to python".casefold()

v_count=0
c_count=0
vowels="aeiou"
alpha="abcdefghijklmnopqrstuvwxyz"

for ch in text:

    if ch in vowels:

        v_count=v_count+1

    elif ch.isalpha():

        c_count+=1

        

print(f"vowels={v_count} consonents={c_count}")



