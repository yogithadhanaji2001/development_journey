# for i in range (1,6):

#     for j in range (1,i+1):

#         print("*", end="\t" )

#     print()    


# half pyramid

for row in range (1,6):

    for sp in range (1,7-row) :

        print(" ", end=" ")

    for col in range(1,row+1):
        print("* ", end="")  

    print()
