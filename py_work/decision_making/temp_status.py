# read 3 mark out of 50 per each subject
# calculate total

# base on total display 
# total >140 good
# 130-140 avg
# <130 poor

# read temp in deg cel

# display

# cold => <10deg


temp = int(input("enter temp"))

if temp <10:
    print("cold")

elif  temp<20:
    print("cool") 

elif temp<25:
    print("mild")   

elif temp<30:
    print ("warm")

elif temp <35:
    print("hot")

else:
    print("very hot")   

