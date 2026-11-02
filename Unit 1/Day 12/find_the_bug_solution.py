# ICD2O Lesson 10 micro-game: Find the Bug (TEACHER SOLUTION, do not post)
# The six bugs in find_the_bug.py, in the order students meet them:
#   1. Line 13: def coin_points(coins, level) has no colon            SYNTAX  (SyntaxError: expected ':')
#   2. Line 28: print("Silver") is not indented under the elif        SYNTAX  (IndentationError)
#   3. Line 38: coin_point(coins, level) is misspelt                  RUNTIME (NameError, crashes on level 1)
#   4. Line 42: lives_after_hits(lives, 2) is missing has_shield      RUNTIME (TypeError: missing 1 required positional argument)
#   5. Line 37: total = 0 is inside the loop                          LOGIC   (Total score: 75, should be 130)
#   6. Lines 26, 28, 30: rank_for prints instead of returning         LOGIC   (prints Bronze, then Rank: None)
# Line numbers are for the original file. Deleting line 37 moves every later line up by one.
# After bug 5 is fixed, bug 6 shows Silver, then Rank: None.


def coin_points(coins, level):
    return coins * 5 * level


def lives_after_hits(lives, hits, has_shield):
    if has_shield:
        return lives
    else:
        return lives - hits


def rank_for(score):
    if score >= 200:
        return "Gold"
    elif score >= 100:
        return "Silver"
    else:
        return "Bronze"


lives = 3
total = 0
for level in range(1, 4):
    coins = level + 2
    points = coin_points(coins, level)
    total = total + points
    print("Level", level, "coins:", coins, "points:", points)

lives = lives_after_hits(lives, 2, False)
print("Lives left:", lives)
print("Total score:", total)
print("Rank:", rank_for(total))
