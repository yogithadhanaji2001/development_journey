path = "C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\word.txt"

words=["hello", "hai" ,"madam","racecar","panagram"]

fw=open(path,"w")


for w in words:

    if w==w[::-1]:

        fw.write(w+"\n")




    