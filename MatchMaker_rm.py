Introduction= '''
______________________________
    Welcome to Matchmaker!
We will first ask you some questions
 in order to see your desired response 
  Upon your response, we will give you 
  a score based on your compatibility 
  with myself. Lets see if you have what 
  it takes!
_______________________________
'''
Question = [
    'Baseball is the greatest sport'
    'Math is extremely boring'
    'I enjoy going on adventures'
    'I love meeting new people'
    'My favorite type of food is Italian'
]

Desired_Response = [
    5,
    1,
    5,
    3,
    4
]

Max_Score = 25

import os
import time

os.system('clear')
print(Introduction)

response = []
compatibility = []

for i in range(len(Question)):
    userResponse = int(input(Question))
    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - Desired_Response[i])
    compatibility.append(questionCompatibility)

    print("Question %d compatibility: %d\n" %(i+1, questionCompatibility))

totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c

totalCompatibility *= 100 /Max_Score

print("Calculating Compatibility Score.")
time.sleep(2)
print("Total Compatibility: %d\n\n" %(totalCompatibility))