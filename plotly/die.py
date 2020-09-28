from random import randint

class Die:
    """Class representing a single die."""
    def __init__(self, num_sides=6):
        """Assumes die has six sides, unless specified otherwise."""
        self.num_sides = num_sides

    def roll(self):
        """
        Simulate rolling a die by returning a random number
        between 1 and number of sides.
        """
        return randint(1, self.num_sides)
