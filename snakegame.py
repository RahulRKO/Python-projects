import random

def gameresult(pc,you):
    if pc==you:
        return None
    elif pc=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif pc=="w":
        if you=="g":
            return False
        elif you=="s":
            return True            
    elif pc=="g":
        if you=="s":
            return False
        elif you=="w":
            return True



print("pc Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    pc = 's'
elif randNo == 2:
    pc = 'w'
elif randNo == 3:
    pc = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?: ")
a = gameresult(pc, you)

print(f"Computer chose {pc}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")            
