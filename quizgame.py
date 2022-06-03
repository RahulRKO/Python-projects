print("Welcome to quiz")

wanna_play=input("interested to play the quiz? ").lower()

if wanna_play!="yes":
    print("ig you dont wanna play.")
    quit()  #if they dont type yes simply quit/terminate the program

print("let's play then!!!")
print('''Instructions: 
        1) You need to type answers
        2) you can use capitalcase/smallcase letters only''')

score=0
answer=input("Full form of Ram? ").lower()
if answer=="random access memory":
    print("correct answer!!")
    score+=10
else:
    print("incorrect answer,better luck next time")    

answer2=input("full form of cpu?").lower()
if answer2=="central processing unit":
    print("correct answer!!")
    score+=10
else:
    print("incorrect answer!!,better luck next time")    
print("Your score: ",score)