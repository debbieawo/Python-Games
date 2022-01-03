#Version 2 of Interview Program
import random

candidateInput = []
answerList = []
questionsList = []
jobPoints = 0
jobAnswerGood = "Got the JOB!!! Congratulations!"
jobAnswerMeh = "You didn't get the job, Thank you for interviewing!"

print("Welcome to your Technical Interview!I am interviewing you for an AWS Cloud position, Please answer the following questions")

with open("C:/Users/debbi/OneDrive/Documents/GitHub/100-Days-of-Python/questions.txt") as qA: 
    questionsAnswers = qA.readlines()

for i in range(0, len(questionsAnswers)):
    if(i % 2 == 0 ):
        questionsList.append(questionsAnswers[i])
    else:
        answerList.append(questionsAnswers[i].lower())

combinedList = []
for i in range(0, len(questionsList)):
    t = (questionsList[i],answerList[i])
    combinedList.append(t)

interviewQuestions = random.sample(combinedList,6)

for i in range(0, len(interviewQuestions)):
    candidateInput.append(input(interviewQuestions[i][0]).lower())
    if candidateInput[-1] == interviewQuestions[i][1].strip():
        jobPoints +=1
        print("CORRECT")
    elif interviewQuestions[i][1].strip() == "*":
        jobPoints +=1
        print("PASS")

if jobPoints >= 5:
    print("Thank you for answering all the questions in the technical interview! You ", jobAnswerGood)
else:
    print("Thank you for answering all the questions in the technical interview! You ", jobAnswerMeh)

print("You got a total of ", jobPoints, "points")


