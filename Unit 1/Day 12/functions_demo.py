# # ICD2O Lesson 10: Functions
# # Live demo. Walk through one section at a time.
# # Predict what the player will see BEFORE you run.

# # ------------------------------------------------------------
# # SECTION 0: The problem
# # The same shield rule is copied for the spike, the lava and the enemy.
# # Change the rule and you have to change it in three places.
# # ------------------------------------------------------------
# print("=== Section 0: copy and paste ===")
# lives = 10
# has_shield = True

# spike_hit = 2
# if has_shield:
#     lives = lives - spike_hit // 2
# else:
#     lives = lives - spike_hit

# lava_hit = 5
# if has_shield:
#     lives = lives - lava_hit // 2
# else:
#     lives = lives - lava_hit

# enemy_hit = 3
# if has_shield:
#     lives = lives - enemy_hit // 2
# else:
#     lives = lives - enemy_hit

# print("Lives:", lives)

# # ------------------------------------------------------------
# # SECTION 1: def, and calling a function
# # def gives a block of code a name. The block runs only when it is called.
# # A call is the name followed by brackets.
# # ------------------------------------------------------------
# print("=== Section 1: def and call ===")


# def show_title():
#     print("*** STUDIO GAME ***")
#     print("Press SPACE to start")


# print("Before the call")
# show_title()
# show_title()
# print("After the calls")

# # ------------------------------------------------------------
# # SECTION 2: Parameters
# # A parameter is a variable in the def line.
# # At the call, it gets the value in the brackets (the argument).
# # ------------------------------------------------------------
# print("=== Section 2: parameters ===")


# def show_lives(lives_to_show):
#     print("Lives:", lives_to_show)


# show_lives(3)
# lives_left = 1
# show_lives(lives_left)


# def show_score(player_name, score):
#     print(player_name, "has", score, "points")


# show_score("Ava", 40)
# show_score("Ben", 75)

# # ------------------------------------------------------------
# # SECTION 3: return
# # return sends a value back to the line that called the function.
# # The function stops at return. Store the value or use it straight away.
# # ------------------------------------------------------------
# print("=== Section 3: return ===")


# def damage_after_shield(hit, has_shield):
#     if has_shield:
#         return hit // 2
#     else:
#         return hit


# lives = 10
# lives = lives - damage_after_shield(2, True)     # spike
# lives = lives - damage_after_shield(5, True)     # lava
# lives = lives - damage_after_shield(3, True)     # enemy
# print("Lives with a shield:", lives)

# lives = 10
# damage = damage_after_shield(5, False)
# print("Lava without a shield does", damage)
# lives = lives - damage
# print("Lives:", lives)

# # ------------------------------------------------------------
# # SECTION 4: A function can give back a bool or a str
# # ------------------------------------------------------------
# print("=== Section 4: bool and str ===")


# def can_open_door(has_key, score, score_needed):
#     return has_key and score >= score_needed


# def rank_for(score):
#     if score >= 100:
#         return "Gold"
#     elif score >= 50:
#         return "Silver"
#     elif score >= 10:
#         return "Bronze"
#     else:
#         return "No rank yet"


# if can_open_door(True, 20, 30):
#     print("The door opens.")
# else:
#     print("The door stays shut.")

# print("Rank for 75:", rank_for(75))
# print("Rank for 5:", rank_for(5))

# # ------------------------------------------------------------
# # SECTION 5: Calling a function inside a loop
# # The accumulate pattern, with the function doing the work for each level.
# # ------------------------------------------------------------
# print("=== Section 5: functions in a loop ===")


def coins_for_level(level):
    return level * 10


total = 0
for level in range(1, 4):
    coins = coins_for_level(level)
    print("Level", level, "gives", coins, "coins")
    total = total + coins
print("Total:", total)

# # ------------------------------------------------------------
# # SECTION 6: Traps. Uncomment ONE at a time.
# # ------------------------------------------------------------
# print("=== Section 6: traps ===")

# # Trap 1: print instead of return.
# # The function prints "Silver", then gives back None.
# # def bad_rank(score):
# #     if score >= 50:
# #         print("Silver")
# #     else:
# #         print("Bronze")
# #
# # print("Rank:", bad_rank(75))

# # Trap 2: the returned value goes nowhere.
# # lose_life gives back 2, but nothing stores it. lives is still 3.
# # def lose_life(lives):
# #     lives = lives - 1
# #     return lives
# #
# # lives = 3
# # lose_life(lives)
# # print("Lives:", lives)

# # Trap 3: the wrong number of values in the call (TypeError).
# # print(damage_after_shield(4))

# # Trap 4: a variable made inside a function does not exist outside it (NameError).
# # def find_bonus(level):
# #     bonus = level * 5
# #     return bonus
# #
# # find_bonus(2)
# # print(bonus)

# # Trap 5: calling a function above its def (NameError).
# # Move this line to the very top of the file and run.
# # show_title()
