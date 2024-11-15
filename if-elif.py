feedback1 =int(input("Please Enter the feedback of student 1: "))
feedback2 =int(input("Please Enter the feedback of student 2: "))
feedback3 =int(input("Please Enter the feedback of student 3: "))
feedback4 =int(input("Please Enter the feedback of student 4: "))
feedback5 =int(input("Please Enter the feedback of student 5: "))
average =(feedback1+feedback2+feedback3+feedback4+feedback5)/5
print("*****************Part 1 of the prograam**********")
if(average > 3):
    print("your rating is Good which is ",average)
else:
    print("your rating is poor which is",average) 

print("*****************Part 2 of the prograam**********")
if(average > 4):
    print("very Good your rating is",average)
elif(average>4):
    print(" Average your rating is",average)
elif(average>2):
    print("Average is poor this is",average)
else:
    print("Work on the quality")


