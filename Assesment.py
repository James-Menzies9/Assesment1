import easygui as e
import random

player_name = e.enterbox("Whats your name?")
print(player_name) 
e.msgbox("There is a total of 8 question you have to answer")
print("There is a total of 8 question you have to answer")

e.msgbox ("Welcome to the quiz")
print ("Welcome to the quiz")
#asks for players age
player_age=e.integerbox("How old are you","Age")
print(player_age)

#says if you can or can not play this game
if 15 <= player_age <= 18:
    e.msgbox("You can now continue to take the quiz")
    print("You can now continue to take the quiz")
else:
    #keeps you in an endless loop
    while True:
        e.msgbox("You can't play this game")
#Answer for question in list form
answers=[99,random.randint (1,10),str(random.randint(1,50)),str("2/9/1945") and str("2 September 1945"),"Elon Musk","automatable manufacturer","The land","4pm"]      
#keeps them in the loop until all the answers are correct
while True:
        score = 0
        e.msgbox("Question 1")
        print("Question 1")
        print(score)
        #Askes question
        Question1 = e.integerbox("What is 100x12/12-1","Question 1")
        print(Question1)
        #says if your right or wrong and if you get correct you get a point (same for every question)
        if Question1 == answer[0]:
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")
        e.msgbox(score,Score)
        print(score)

        
        e.msgbox("Question 2")
        print("Question 2")
        Question2 = e.integerbox("Pick a number between 1 and 10","Question 2")
        print(Answer2)
        if Question2 == answer[1]:
            score +=1
            e.msgbox("Correct")
            print("Correct")
        else:
            e.msgbox("Incorrect")
            print("Incorrect")

        e.msgbox(score,Score)
        print(score)

        
        wrong = str(random.randint(1,50))
        wrong2 = str(random.randint(1,50))
        e.msgbox("Question 3")
        print("Question 3")
        Question3 = e.buttonbox("Pick the right number","Question3",choices=[wrong,wrong2,Answer3])

        if Question3 == answer[2]:
            score +=1
            e.msgbox("Correct")
            print("Correct")
        else:
            e.msgbox("Incorrect")
            print("Incorrect")
            print(score)
        e.msgbox( score)
        #Turns number into strings so theres no math calculation 
        e.msgbox("Question 4")
        print("Question 4")

        Question4 = e.enterbox("When did World War 2 official end")
        if str(Question4) == answer[3]:
            e.msgbox("Correct")
            print("Correct")
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")
            print(score)

        e.msgbox(score,Score)
        print(score)

        e.msgbox("Question 5")
        print("Question 5")

        Question5 = e.enterbox("Who owns SpaceX")
        if Question5 == answer[4]:
            e.msgbox("Correct")
            print("Correct")
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")

        e.msgbox(score,Score)
        print(score)

        e.msgbox("Question 6")
        print("Question 6")

        Question6 = e.buttonbox("What is a BMW","Question 6",choices=("Pickup truck","automatable manufacturer","True supercar"))
        if Question6 == answer[5]:
            e.msgbox("Correct")
            print("Correct")
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")

        e.msgbox(score,Score)
        print(score)

        e.msgbox("Question 7")
        print("Question 7")

        Question7 = e.buttonbox("Where does Mcdonalds gets most of its networth from","Question 7",choices=("The land","The food","Sponsers"))

        if Question7 == answer[6]:
            e.msgbox("Correct")
            print("Correct")
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")

        e.msgbox(score,Score)
        print(score)

        e.msgbox("Question 8")
        print("Question 8")

        Question8 = e.buttonbox("What time is 1600 in 12 hour time","Question 8",choices=("6am","2pm","4pm"))
        e.msgbox(score,Score)
        print(score)

        if Question8 == answer[7]:
            e.msgbox("Correct")
            print("Correct")
            score +=1
        else:
            e.msgbox("Incorrect")
            print("Incorrect")

        e.msgbox(score,Score)
        print(score)
        #Thanks them for playing and a differnt message depending on the ammount of right answers you got 0=
        e.msgbox("thanks for playing " + player_name)
        print("thanks for playing " + player_name)
        if score == 8:
            e.msgbox("Well done you got all the question correct")
            break
        elif score < 4:
            e.msgbox("Good try, try to get a better score.")
        else:
            e.msgbox("Good job you got over half correct")