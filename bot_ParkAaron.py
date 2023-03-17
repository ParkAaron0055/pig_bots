import random
import os

# Two players, 0 and 1
# 0 = human
# 1 = computer

scores = [0, 0]  # both players' scores

def show_scores():
    # Call this to print out the scores
    print("-" * 20)
    print(f"Human: {scores[0]}")
    print(f"Computer: {scores[1]}")
    print("-" * 20)

def player_choice(player, score):
    # TODO: return True if the player wants to roll again
    #       return False if the player wants to hold
    if player == 0:
 #       var = (input("You going again? Remember 99% of gamblers quit before their first big win. y/n:"))
  #      if var == "y":
   #         return True
    #    else:
     #       return False

        if scores[0] - scores[1] > 20:
            if score >= 30:
                return False
            else:
                return True
        elif scores[0] > scores[1] + 20:
            if score >= 23:
                return False
            else:
                return True
        elif scores[0] > scores[1]:
            if score >= 15:
                return False
            else:
                return True
        elif scores[1] + 20 > scores[0]:
            if score >= 10:
                return False
            else:
                return True
        elif scores[0] == scores[1]:
            if score >= 22:
                return False
            else:
                return True
        else:
            return False
    if player == 1:
        if scores[0] - scores[1] > 15:
            if score >= 18:
                return False
            else:
                return True
        elif scores[0] > scores[1] + 12:
            if score >= 10:
                return False
            else:
                return True
        elif scores[0] > scores[1]:
            if score >= 19:
                return False
            else:
                return True
        elif scores[1] + 17 > scores[0]:
            if score >= 15:
                return False
            else:
                return True
        elif scores[0] == scores[1]:
            if score >= 12:
                return False
            else:
                return True
        else:
            return False
    pass

def take_turn(player):
    round_score = 0
    while True:
        die = random.randint(1,6)
        print(die)
        if die == 1:
            round_score = 0
            break
        else:
            round_score += die
        if not player_choice(player,round_score):
            break

    scores[player] += round_score
    # Leave this at the end of the function
    print(f"Points earned this turn: {round_score}")
    input("Turn is over. Press  to continue.")

# Don't edit below here.
turn = 0  # whose turn is it?
# This loop will alternate between players taking turns
playing = True  # this becomes False when the game ends at 100 pts
while playing:
    os.system("clear")
    show_scores()
    take_turn(turn)
    if max(scores) >= 100:
        playing = False
    turn = 1 if turn == 0 else 0

print("Final scores:")
show_scores()
