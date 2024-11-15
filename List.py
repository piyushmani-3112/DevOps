# LIst can store any combination of data
Count = 1
sum = 0
name=[]
feedback=[]
while(Count<=5):
    Count = Count+1
    StudentName=input("Enter Your Name of student ")
    name.append(StudentName)
    feedbackValue=int(input("Enter Your Feedback of student "))
    feedback.append(feedbackValue)
    sum = sum + feedbackValue
average = sum/5
if(average>4):
    print("very Good your rating is",average)
elif(average>4):
    print(" Average your rating is",average)
elif(average>2):
    print("Average is poor this is",average)
else:
    print("Work on the quality")

for index in range(0,len(name)):
    print("Name of Student is ",name[index])
    print("Feedback of student is ",feedback[index])

# LIst can store any combination of data
sum = 0
name=[]
feedback=[]
flag = "Yes" # -> For an Infinite Loop
while(flag=="Yes"):
    StudentName=input("Enter Your Name of student ")
    name.append(StudentName)
    feedbackValue=int(input("Enter Your Feedback of student "))
    feedback.append(feedbackValue)
    sum = sum + feedbackValue
    flag =input("Do you want to proceed Enter Yes/No ")
average = sum/5
if(average>4):
    print("very Good your rating is",average)
elif(average>4):
    print(" Average your rating is",average)
elif(average>2):
    print("Average is poor this is",average)
else:
    print("Work on the quality")

for index in range(0,len(name)):
    print("Name of Student is ",name[index])
    print("Feedback of student is ",feedback[index])