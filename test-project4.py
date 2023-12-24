for i in range(5):
    import random
    num=random.randint(1,5)
    x=int(input("Enter Number:"))
    if num==x:
        print("you Win Congratulations :")
        break
    elif num>x:
        print("Too Low")
    elif num<x:
        print("Too High")
print("Game Over:")