from die import Die

#Create a D6.
die = Die()

#Create a list to store roll results.
results = []

#Make rolls and store results in results list.
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

#Analyze results of rolls.

#Create a list for frequencies.
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
