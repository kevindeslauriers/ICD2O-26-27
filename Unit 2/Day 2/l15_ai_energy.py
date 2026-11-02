# ICD2O Lesson 15: How much do our AI prompts cost the planet?
# Change the three numbers below to match your class, then run it.

students = 5
prompts_per_day = 10       # each student, each school day (your estimate)
school_days = 180

total_prompts = students * prompts_per_day * school_days
print("Prompts in one school year:", total_prompts)
print()

# Google (2025): median Gemini text prompt. Counts answering prompts only, not training.
energy_per_prompt = 0.24   # watt-hours
water_low = 0.26           # millilitres (about five drops)

# A 2023 research estimate: 10 to 50 mL of water per prompt (we use the top of the range)
water_high = 50            # millilitres

energy = total_prompts * energy_per_prompt
print("Energy:", energy, "watt-hours")
print("That runs a 10 watt LED bulb for", energy // 10, "hours")
print()

water_ml_low = total_prompts * water_low
water_ml_high = total_prompts * water_high
print("Water, Google estimate:", water_ml_low // 1000, "litres")
print("That is about", water_ml_low // 500, "water bottles")
print("Water, 2023 estimate:", water_ml_high // 1000, "litres")
print("That is about", water_ml_high // 500, "water bottles")
