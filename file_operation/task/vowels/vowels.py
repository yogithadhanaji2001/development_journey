path= "C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\task\\vowels\\words.txt"


fr= open(path,"r")

vowels={"a","e","i","o","u"}


for ch in fr:
    # print(ch)

    word=ch.strip().lower()

    if word and word[0] in vowels:

        print(ch)
