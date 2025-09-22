all_path ="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\students\\all_students.txt"
failed_path ="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\students\\failed_students.txt"
passed_path= "C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\students\\passed_students.txt"


fr_all=open(all_path,"r")
fr_fail=open(failed_path,"r")
fw_pass=open(passed_path,"w")


all_students_set=set()
failed_student_set=set()

for ch in fr_all:

    all_students_set.add(ch.rstrip("\n"))



for ch in fr_fail:

    failed_student_set.add(ch.rstrip("\n"))


passed_student=all_students_set.difference(failed_student_set)

for ch in passed_student:

    fw_pass.write(ch+"\n")