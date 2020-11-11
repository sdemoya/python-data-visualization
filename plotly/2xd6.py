from die_class import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


#Create dice.
die1 = Die()
die2 = Die()

#Create a list to store roll results.
results = []

#Make rolls and store results in results list.
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

print(results)

#Analyze results of rolls.

#Create a list for frequencies.
frequencies = []

max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Create a histogram.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of Rolling two D6 dice 1000 Times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2xd6.html')

