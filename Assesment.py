import easygui as e 

e.msgbox ("Welcome to the quiz")
print ("Welcome to the quiz")

player_age=e.integerbox("How old are you","Age")
print(player_age)

if player_age < 12:
    e.msgbox("you are to young to take the quiz")
    print("you are to young to take the quiz")
else:
    e.msgbox("you can now continue to take the quiz")
    print("you can now continue to take the quiz")

Score = 0 
e.msgbox("There is a total of 8 question you have to answer")
print("There is a total of 8 question you have to answer")

e.msgbox("Question 1")
print("Question 1")
print("Current score",Score)
Answer1 = 100
Question1 = e.integerbox("What is 100x12/12","Question 1")
print(Question1)
if Question1 == Answer1:
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")
msgbox("New score",Score)
print(Score)

Answer2 = 
#e.msgbox("Question 2")
#print("Question 2")

#e.msgbox("Question 3")
#print("Question 3")

#e.msgbox("Question 4")
#print("Question 4")

#e.msgbox("Question 5")
#print("Question 5")

#e.msgbox("Question 6")
#print("Question 6")

#e.msgbox("Question 7")
#print("Question 7")

#e.msgbox("Question 8")
#print("Question 8")

