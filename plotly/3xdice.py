#import from plotly
from plotly.graph_objects import Bar, Layout
from plotly import offline

#import Dice class
from die_class import Die

#create dice
die1 = ()
die2 = (20)
die3 = (10)

#create list to store results in
results = []

#use for loop to "roll" dice
for roll in range(1000):
    result = die1.num_sides + die2.num_sides + die3.num_sides
    results.append(result)

#create list to record frequency of each roll
frequencies = []

#set max_result to make code more re-usable
max_result = die1.num_sides + die2.num_sides + die3.num_sides

#use for loop to analyze results/count frequencies
for num in range(3, max_result+1):
    frequency = results.count(num)
    frequencies.append(frequency)

#set x values for histogram
x_values = list(range(3, max_results+1))

#set data here
