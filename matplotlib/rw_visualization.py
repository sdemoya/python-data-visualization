import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Create a random walk.
rw = RandomWalk()
rw.fill_walk()

# Style plot/figure.
plt.style.use('dark_background')

# Plot the walk's points.
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

# Open viewer.
plt.show()

# Save plot/figure to a png.
plt.savefig('random_walk.png', bbox_inches='tight')
