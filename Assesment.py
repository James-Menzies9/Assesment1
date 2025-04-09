import easygui as e
import random 

e.msgbox ("Welcome to the quiz")
print ("Welcome to the quiz")
#asks for players age
player_age=e.integerbox("How old are you","Age")
print(player_age)

#says if you can or can not play this game
if player_age  >15 <18:
        e.msgbox("you can now continue to take the quiz")
        print("you can now continue to take the quiz")
if <15 or >18:
    while True:
        e.msgbox("you can't play this game")

    #saves players name for the end of the game           
    player_name = e.enterbox("Whats your name?")
    print(player_name)
    Score = 0 
    e.msgbox("There is a total of 8 question you have to answer")
    print("There is a total of 8 question you have to answer")
#keeps them in the loop until all the answers are correct
while True:
    e.msgbox("Question 1")
    print("Question 1")
    print("Current score",Score)
    #Answer for question
    Answer1 = 99
    #Askes question
    Question1 = e.integerbox("What is 100x12/12-1","Question 1")
    print(Question1)
    #says if your right or wrong and if you get correct you get a point (same for every question)
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

    Answer6 ="automatable manufacturer"
    e.msgbox("Question 6")
    print("Question 6")

    Question6 = e.buttonbox("What is a BMW","Question 6",choices=("Pickup truck","automatable manufacturer","True supercar"))
    if Question6 == Answer6:
        e.msgbox("Correct")
        print("Correct")
        Score +=1
    else:
        e.msgbox("Incorrect")
        print("Incorrect")

    e.msgbox("New score",Score)
    print(Score)

    Answer7 ="The land"
    e.msgbox("Question 7")
    print("Question 7")

    Question7 = e.buttonbox("Where does Mcdonalds gets most of its networth from","Question 7",choices=("The land","The food","Sponsers"))

    if Question7 == Answer7:
        e.msgbox("Correct")
        print("Correct")
        Score +=1
    else:
        e.msgbox("Incorrect")
        print("Incorrect")

    e.msgbox("New score",Score)
    print(Score)

    Answer8 ="4pm"
    e.msgbox("Question 8")
    print("Question 8")

    Question8 = e.buttonbox("What time is 1600 in 12 hour time","Question 8",choices=("6am","2pm","4pm"))
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
    #Thanks them for playing and a differnt message depending on the ammount of right answers you got 0=
    e.msgbox("thanks for playing " + player_name)
    print("thanks for playing " + player_name)
    if Score == 8:
        e.msgbox("Well done you got all the question correct")
        break
    elif score < 4:
        e.msgbox("Good try, try to get a better score.")
    else:
        e.msgbox("Good job you got over half correct")