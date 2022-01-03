#interview program
jobPoints = []
jobAnswerGood = "Got the JOB!!! Congratulations!"
jobAnswerMeh = "You didn't get the job, Thank you for interviewing!"

print("Welcome to your Technical Interview!I am interviewing you for an AWS Cloud position, Please answer the following questions")

custInput1 = input("Describe yourself in three words, input them separated by commas")
custInput2 = input("What technical skills do you have? Input them separated by commas")
custInput3 = input("What AWS Service is an object storage service responsible for storing and retrieving any amount of data anywhere on the internet?")
custInput4 = input("What is AWS' orchestration services that is used in EC2, S3, SNS, CloudWatch, and autoscaling?")
custInput5 = input("What is AWS' data warehouse solution with business intelligence tools?")
custInput6 = input("What is the phonebook of the internet?")

if custInput3 == "S3":
    print("Great answer")
    jobPoints.append(custInput3)
else: 
    print("Thank you for your answer.")
if custInput4 == "Elastic Beanstalk":
    print("Good reply!")
    jobPoints.append(custInput4) 
else: 
    print("Thank you for your answer.")
if custInput5 == "Redshift":
    print("Good answer!")
    jobPoints.append(custInput5)
else: 
    print("Thank you for your answer.")
if custInput6 == "DNS":
    print("Great reply!")
    jobPoints.append(custInput6)
else: 
    print("Thank you for your answer.")

if len(jobPoints) >= 3:
    print(jobAnswerGood)
else:
    print(jobAnswerMeh)


print("Thank you for answering all the questions in the technical interview! You ", jobAnswerGood)


