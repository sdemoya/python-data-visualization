from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8 dice.
die1 = Die(8)
die2 = dice(8)

# Roll the dice, and store the results in a list.
results = []
for roll_num in range(10_000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

