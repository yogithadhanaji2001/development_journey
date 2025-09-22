path="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\task\\leap_year\\years.txt"

fr=open(path,"r")

for line in fr:

    year=int(line.strip("\n"))

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        print(year)
    