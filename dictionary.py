student={"name":"Piyush",
         "feedback":3,
         "address":
         {"city":"Noida",
          "state":"UP",
          "pin":201301}
          }
print(student["name"])
print(student["feedback"])
print(student["address"]["pin"])

detail = {"key":"value"} # key and value

# List of dictionary

students1=[{"name":"sanjoy","feedback":3}, 
          {"name":"john","feedback":4},
          {"name":"jane","feedback":5}]
print(students1[1]["feedback"])

sum=0
###defining the list of dictionary for students
students=[]
userFlag="Y"
##they are connected through index
##

while(userFlag=="Y"):
    ##creating a dictionary for a new student
    student={}
    name=input("Enter the name of the student")
    student["name"]=name
 #   feedback=int(input("Enter the feedback of the student one by one"))
    feedbackAvailable=input("Do you want to provide feedback? Enter Y or N")
    if(feedbackAvailable=="Y"):
        feedback=int(input("Enter the feedback of the student one by one"))
        student["feedback"]=feedback
    userFlag=input("Do you want to continue? Enter Y or N")
    ##adding the student to the list of students
    print(student)
    students.append(student)
    sum=sum+feedback
print(students)
average=sum/len(students)

if(average>4):
    print("Very good")
elif(average>3):
    print("Average feedback is  average")
elif(average>2):
    print("average feedback is bad")
else:
    print("replace the teacher")

print("#########Feedback of the students#########")
for student in students:
    print("the name of the student is",student["name"])
    print("the feedback of the student is",student["feedback"])

sum=0
###defining the list of dictionary for students
students=[]
userFlag="Y"
##they are connected through index
##

while(userFlag=="Y"):
    ##creating a dictionary for a new student
    student={}
    name=input("Enter the name of the student")
    student["name"]=name
    feedback=int(input("Enter the feedback of the student one by one"))
    student["feedback"]=feedback
    userFlag=input("Do you want to continue? Enter Y or N")
    ##adding the student to the list of students
    print(student)
    students.append(student)
print(students)    
search =input("Enter the Name of the student ")
for student in students:
    if student["name"] == search: #== is for the comarision and = for assigning a value
        print(student["feedback"])
    else:
        print("This guy is not our student")