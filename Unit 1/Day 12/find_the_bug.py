# ICD2O Lesson 10 micro-game: Find the Bug
# This program has 6 bugs: 2 syntax errors, 2 runtime errors and 2 logic errors.
# Fix ONE bug at a time. Run after every fix. Fill in the bug log on your sheet.
#
# When every bug is fixed, the player sees exactly this:
#   Level 1 coins: 3 points: 15
#   Level 2 coins: 4 points: 40
#   Level 3 coins: 5 points: 75
#   Lives left: 1
#   Total score: 130
#   Rank: Silver

def coin_points(coins, level)
    return coins * 5 * level


def lives_after_hits(lives, hits, has_shield):
    if has_shield:
        return lives
    else:
        return lives - hits


def rank_for(score):
    if score >= 200:
        print("Gold")
    elif score >= 100:
    print("Silver")
    else:
        print("Bronze")


lives = 3
total = 0
for level in range(1, 4):
    coins = level + 2
    total = 0
    points = coin_point(coins, level)
    total = total + points
    print("Level", level, "coins:", coins, "points:", points)

lives = lives_after_hits(lives, 2)
print("Lives left:", lives)
print("Total score:", total)
print("Rank:", rank_for(total))
