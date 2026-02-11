import random
import copy


class Hat:
    """
    A Hat object that contains colored balls.
    Balls are stored as strings inside a list.
    Example: Hat(red=2, blue=1) -> ['red', 'red', 'blue']
    """

    def __init__(self, **kwargs):
        """
        Initialize the hat with colored balls.
        Each keyword represents a color and its quantity.
        """
        self.contents = []

        # Add each color into the contents list based on its quantity
        for color, quantity in kwargs.items():
            for _ in range(quantity):
                self.contents.append(color)

    def draw(self, num_of_ball):
        """
        Randomly draw balls from the hat without replacement.

        Parameters:
        num_of_ball (int): Number of balls to draw.

        Returns:
        list: The balls that were drawn.
        """
        removed_balls = []

        # If requested more balls than available,
        # return all remaining balls.
        if num_of_ball > len(self.contents):
            return self.contents.copy()

        # Randomly remove balls one by one
        for _ in range(num_of_ball):
            choice = random.choice(self.contents)
            self.contents.remove(choice)
            removed_balls.append(choice)

        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform a Monte Carlo simulation to estimate probability.

    Parameters:
    hat (Hat): A Hat object containing balls.
    expected_balls (dict): Expected ball counts (e.g., {"red": 2}).
    num_balls_drawn (int): Number of balls drawn per experiment.
    num_experiments (int): Number of simulation trials.

    Returns:
    float: Estimated probability of drawing at least the expected balls.
    """

    success_count = 0  # Track successful experiments

    # Repeat experiment multiple times
    for _ in range(num_experiments):

        # Use deep copy to avoid modifying original hat
        hat_copy = copy.deepcopy(hat)

        # Draw balls
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # Count how many of each color were drawn
        drawn_counts = {}
        for ball in balls_drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if drawn result satisfies expected condition
        success = True
        for color, required_count in expected_balls.items():
            if drawn_counts.get(color, 0) < required_count:
                success = False
                break

        # If condition satisfied, increment success counter
        if success:
            success_count += 1

    # Probability = successful experiments / total experiments
    return success_count / num_experiments
