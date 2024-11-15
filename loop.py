number=1
while(number<=5):
    print(number)
    number=number+1
#If number >0 it will go to infinite loop if number > 5 Loop will not run
for number in range(11,15,1): #(start of the index,maximum value,incremental value)
    print(number)

student_Count = 1
sum = 0
while(student_Count <=5):
    student_Count = student_Count+1
    feedback=int(input("Enter Your feedback student "))
    sum = sum + feedback
average = sum/5
if(average>4):
    print("very Good your rating is",average)
elif(average>4):
    print(" Average your rating is",average)
elif(average>2):
    print("Average is poor this is",average)
else:
    print("Work on the quality")
    