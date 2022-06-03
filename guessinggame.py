import random
upper_bound=input("enter the upper bound number: ")

if upper_bound.isdigit():
    upper_bound=int(upper_bound)
    if upper_bound<=0:
        print("enter a number greater than 0")
        quit()
else:
    print("enter a valid number next time.") 
    quit()   
n=random.randint(0,upper_bound)

guessed_number=(input("guess the number: "))
no_of_guesses=0
if guessed_number.isdigit():
    guessed_number=int(upper_bound)
    if guessed_number<=0:
        print("enter a number greater than 0")
        quit()
else:
    print("enter a valid number next time.") 
    quit()
while guessed_number!=n:
    if guessed_number>n:
        print("guess a smaller number")
        no_of_guesses+=1
    elif guessed_number<n:
        print("guess higher") 
        no_of_guesses+=1   
    guessed_number=int(input("guess again!!"))
if guessed_number==n:
    no_of_guesses+=1
    print("You got it in ",no_of_guesses,"guesses")

