path="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\data.txt"

fw=open(path,"w")

greeting_list = ["good morning", "good afternoon", "good evening"]


for g in greeting_list:

    fw.write(g+"\n")
