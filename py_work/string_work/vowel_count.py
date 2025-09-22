text = "apple orange"
vowels="aeiou"

v_count=0

for ch in text:

    # print (ch)

    if ch in vowels:

        v_count=v_count+1


print(f"vowel count = {v_count}")
    
