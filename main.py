import random
import time

print("You will roll a die. You can keep going as long as you don't get a 1. First to 50 points win")
print(" Ex. I roll a five. I will keeping going to get a four and a three. I can still continue but if I get a 1, my score will be zero.")

comp_score = 0
player_score = 0
comp_times = 0


while True:
    q1 = input("roll or pass ")
    add = random.randrange(1, 6)
    if q1 == "roll":

        if add == 1:
            q1 = "pass"
            player_score = 0
            print("Oops! you rolled a 1")

            # Computer play -------
            while comp_times < 3:
                add1 = random.randrange(1, 6)
                if add1 == 1:
                    comp_score = 0
                    print("Computer rolled a 1. Your turn")
                    q1 = "roll"
                    break
                else:
                    comp_score += add1
                    print(f"Computer's score: {comp_score}")
                comp_times += 1
                time.sleep(2)
                if comp_score >= 50:
                    print("THE COMPUTER WON!! YOU LOST! ")
                    quit()
            comp_times = 0

        else:
            player_score += add
            print(player_score)
            if player_score >= 50:
                print("YOU WON!!!!")
                quit()
    elif q1 == "pass":
        while comp_times < 3:
            add1 = random.randrange(1, 6)
            if add1 == 1:
                comp_score = 0
                print("Computer rolled a 1. Your turn")
                q1 = "roll"
                break
            else:
                comp_score += add1
                print(f"Computer's score: {comp_score}")
            comp_times += 1
            time.sleep(2)
            if comp_score >= 50:
                print("THE COMPUTER WON!! YOU LOST! ")
                quit()
        comp_times = 0


