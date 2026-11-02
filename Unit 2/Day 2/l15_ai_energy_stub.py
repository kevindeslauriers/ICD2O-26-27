# ICD2O Lesson 15: How much do our AI prompts cost the planet?
# The variables are set for you. Write the code for each step below.
# Run your program after each step to check it works before moving on.

students = 5
prompts_per_day = 10       # each student, each school day (change this to your own guess)
school_days = 180

# Google (2025): median Gemini text prompt. Counts answering prompts only, not training.
energy_per_prompt = 0.24   # watt hours
water_low = 0.26           # millilitres (about five drops)

# A 2023 research estimate: 10 to 50 mL of water per prompt (we use the top of the range)
water_high = 50            # millilitres

led_watts = 10             # a 10 watt LED bulb
ml_per_litre = 1000
ml_per_bottle = 500        # one water bottle


# STEP 1: Total prompts
# Make a variable called total_prompts.
# It is students times prompts_per_day times school_days.
# Then print: Prompts in one school year: <total_prompts>



# STEP 2: Energy
# Make a variable called energy.
# It is total_prompts times energy_per_prompt (the answer is in watt hours).
# Print: Energy: <energy> watt hours



# STEP 3: The LED bulb
# How many hours could that energy run the LED bulb?
# Divide energy by led_watts. Use // so you get whole hours.
# Print: That runs a 10 watt LED bulb for <hours> hours



# STEP 4: Water, Google estimate
# Make a variable called water_ml_low: total_prompts times water_low.
# Turn it into litres: water_ml_low // ml_per_litre
# Turn it into water bottles: water_ml_low // ml_per_bottle
# Print both, for example:
#   Water, Google estimate: <litres> litres
#   That is about <bottles> water bottles



# STEP 5: Water, 2023 estimate
# Do the same as Step 4, but with water_high.
# Call the new variable water_ml_high.



# STEP 6: Scale it up
# Change students at the top to 1000000 and run the program again.
# Write your results in the handout table (Part 4).
#
# Check your work: with the starting values (5 students, 10 prompts, 180 days)
# your program should print 9000 prompts, 2160.0 watt hours, 216.0 hours,
# 2.0 litres and 4.0 bottles (Google), and 450 litres and 900 bottles (2023).
