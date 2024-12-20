#beggining
blair_points = 0
serena_points = 0

#middle
answer = input("are you a) messy, or b) organized\n")
if answer == "a":
    serena_points += 1
elif answer == "b":
    blair_points += 1

answer = input("would you rather date a) Chuck, or b) Dan\n")
if answer == "a":
    blair_points += 1
elif answer == "b":
    serena_points += 1

answer = input("are you a) spontaneous, or b) over plan everything\n")
if answer == "a":
    serena_points += 1
elif answer == "b":
    blair_points += 1
    
answer = input("do you like a) classy outfits, or b) chic but casual outfits\n")
if answer == "a":
    blair_points += 1
elif answer == "b":
    serena_points += 1

answer = input("in your teen years you are a) focused on your future, or b) focused on having fun\n")
if answer == "a":
    blair_points += 1
elif answer == "b":
    serena_points += 1

#end
if blair_points > serena_points:
    print("you are more like Blair")
elif serena_points > blair_points:
    print("you are more like Serena")