attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]


print(len(attendance) ,"days")

wording_day=0
leave=0

for a in attendance:

    if a !="H":

        wording_day=wording_day+1

       

print(wording_day)   

for a in attendance:

    if a =="L":
        leave=leave+1

print(leave)        

