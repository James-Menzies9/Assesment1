import easygui as e
import random 

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
Answer1 = 99
Question1 = e.integerbox("What is 100x12/12-1","Question 1")
print(Question1)
if Question1 == Answer1:
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")
e.msgbox("New score",Score)
print(Score)

Answer2 = random.randint (1,10)
e.msgbox("Question 2")
print("Question 2")
Question2 = e.integerbox("Pick a number between 1 and 10","Question 2")
print(Answer2)
if Question2 == Answer2:
    Score +=1
    e.msgbox("Correct")
    print("Correct")
else:
    e.msgbox("Incorrect")
    print("Incorrect")

e.msgbox("New score",Score)
print(Score)

Answer3 = str(random.randint(1,50))
wrong = str(random.randint(1,50))
wrong2 = str(random.randint(1,50))
e.msgbox("Question 3")
print("Question 3")
Question3 = e.buttonbox("Pick the right number","Question3",choices=[wrong,wrong2,Answer3])

if Question3 == Answer3:
     Score +=1
     e.msgbox("Correct")
     print("Correct")
else:
    e.msgbox("Incorrect")
    print("Incorrect")
    print(Score)

Answer4 = str("2/9/1945") and str("2 September 1945")
e.msgbox("Question 4")
print("Question 4")

Question4 = e.enterbox("When did World War 2 official end")
if str(Question4) == Answer4:
    e.msgbox("Correct")
    print("Correct")
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")
    print(Score)

e.msgbox("New score",Score)
print(Score)

Answer5 ="Elon Musk"
e.msgbox("Question 5")
print("Question 5")

Question5 = e.enterbox("Who owns SpaceX")
if Question5 == Answer5:
    e.msgbox("Correct")
    print("Correct")
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")

e.msgbox("New score",Score)
print(Score)

Answer6 =""
e.msgbox("Question 6")
print("Question 6")

Question6 = e.buttonbox("","Question 6",choices=("","",""))
e.msgbox("New score",Score)
print(Score)
if Question6 == Answer6:
    e.msgbox("Correct")
    print("Correct")
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")

e.msgbox("New score",Score)
print(Score)

Answer7 =""
e.msgbox("Question 7")
print("Question 7")

Question7 = e.buttonbox("","Question 7",choices=("","",""))

if Question7 == Answer7:
    e.msgbox("Correct")
    print("Correct")
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")

e.msgbox("New score",Score)
print(Score)

Answer8 =""
e.msgbox("Question 8")
print("Question 8")

Question8 = e.buttonbox("","Question 8",choices=("","",""))
e.msgbox("New score",Score)
print(Score)

if Question8 == Answer8:
    e.msgbox("Correct")
    print("Correct")
    Score +=1
else:
    e.msgbox("Incorrect")
    print("Incorrect")

e.msgbox("New score",Score)
print(Score)

if Score == 8:
    e.msgbox("Well done you got all the question correct")
elif score < 4:
    e.msgbox("Good try, try to get a better score.")
else:
    e.msgbox("Good job you got over half correct")