import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Create a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Style plot/figure.
    plt.style.use('dark_background')

    # Plot the walk's points.
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.com.Blues,
            edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0,0, c='pink', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='purple', edgecolors='none',
            s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Open viewer.
    plt.show()

    keep_running = input("Plot another walk? (y/n):")
    if keep_running == 'n':
        break

# Save plot/figure to a png.
plt.savefig('random_walk.png', bbox_inches='tight')
